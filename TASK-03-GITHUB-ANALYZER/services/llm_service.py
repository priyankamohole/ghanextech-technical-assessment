
import json

from groq import Groq
from pydantic import ValidationError

from config.settings import GROQ_API_KEY, GROQ_MODEL

from services.repository_analyzer import RepositoryAnalysis

from services.prompt_templates import (
    SYSTEM_PROMPT,
    build_analysis_prompt
)


class LLMService:

    def __init__(self):

        if not GROQ_API_KEY:
            raise ValueError(
                "GROQ_API_KEY is missing from .env"
            )

        self.client = Groq(api_key=GROQ_API_KEY)
        self.model = GROQ_MODEL

    def _generate_response(self, messages):

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.1,
            response_format={"type": "json_object"},
            max_completion_tokens=3000
        )
        content = response.choices[0].message.content

        if not content:
            raise RuntimeError("Groq returned an empty response.")

        return content

    def analyze_repository(self, repository_data):

        prompt = build_analysis_prompt(repository_data)

        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            }
        ]

        last_error = None

        # First attempt + two correction attempts
        for attempt in range(3):

            try:

                print(
                    f"AI analysis attempt: {attempt + 1}/3"
                )

                raw_response = self._generate_response(
                    messages
                )

                parsed_response = json.loads(raw_response)

                validated_result = (
                    RepositoryAnalysis.model_validate(
                        parsed_response
                    )
                )

                print("AI response validated successfully!")

                return validated_result

            except (ValidationError, json.JSONDecodeError) as error:

                last_error = error

                print(
                    f"Response validation failed: {error}"
                )

                if attempt == 2:
                    break

                # Ask the model to correct its previous output.
                messages.extend([
                    {
                        "role": "assistant",
                        "content": raw_response
                    },
                    {
                        "role": "user",
                        "content": f"""
Your previous JSON response did not match
the required Pydantic schema.

Validation error:

{str(error)}

Please correct the JSON.

Requirements:
1. Include every required field.
2. Use exact field names.
3. Objects must remain JSON objects.
4. Lists must remain JSON arrays.
5. Recommendations must have all five fields.
6. Contribution opportunities must have all three fields.
7. Provide at least three recommendations.
8. Return ONLY corrected valid JSON.

Original schema:

{json.dumps(RepositoryAnalysis.model_json_schema(), indent=2)}
"""
                    }
                ])

        raise RuntimeError(
            "Unable to generate a valid repository analysis "
            f"after 3 attempts. Last error: {last_error}"
        )
