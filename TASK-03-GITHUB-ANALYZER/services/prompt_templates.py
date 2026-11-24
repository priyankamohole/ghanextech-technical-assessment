
import json

from services.repository_analyzer import RepositoryAnalysis


SYSTEM_PROMPT = """
You are a senior software architect and open-source
repository analyst.

Analyze only the repository evidence supplied by the user.

STRICT OUTPUT REQUIREMENTS:

1. Return ONLY valid JSON.
2. Follow the exact JSON schema supplied.
3. Every required field must be present.
4. Do not rename any JSON keys.
5. Do not replace JSON objects with strings.
6. Do not replace arrays with strings.
7. Recommendations must contain:
   title, problem, suggested_solution, priority, evidence.
8. Contribution opportunities must contain:
   area, opportunity, rationale.
9. Provide at least THREE recommendations.
10. Use High, Medium or Low for priority.
11. Never invent repository files or dependencies.
12. Clearly distinguish facts from inferences.
13. If evidence is insufficient, mention that limitation.
"""


def build_analysis_prompt(repository_data):

    metadata = repository_data["metadata"]

    license_info = metadata.get("license")

    license_name = (
        license_info.get("name")
        if isinstance(license_info, dict)
        else None
    )

    repo_information = {
        "name": metadata.get("full_name"),
        "description": metadata.get("description"),
        "stars": metadata.get("stargazers_count"),
        "forks": metadata.get("forks_count"),
        "open_issues": metadata.get("open_issues_count"),
        "primary_language": metadata.get("language"),
        "license": license_name,
        "topics": metadata.get("topics", []),
        "languages": repository_data.get("languages", {}),
        "readme": repository_data.get("readme", "")[:6000],

        "directory_structure": repository_data.get("directory", [])[:60],

        "package_files": {
            name: content[:3000]
            for name, content in list(
                repository_data.get("packages", {}).items()
            )[:5]
        },
        "tree_truncated": repository_data.get(
            "tree_truncated", False
        )
    }

    schema = RepositoryAnalysis.model_json_schema()

    return f"""
Analyze the following GitHub repository.

REPOSITORY EVIDENCE:

{json.dumps(repo_information, indent=2)}

REQUIRED JSON SCHEMA:

{json.dumps(schema, indent=2)}

Follow this schema exactly.

Generate:
- Executive summary
- Technologies with evidence
- Project strengths
- Architecture analysis
- At least three actionable recommendations
- Contribution opportunities
- Analysis limitations

Remember:
Return arrays as arrays and objects as objects.
Do not omit required fields.
Do not invent unsupported facts.
"""
