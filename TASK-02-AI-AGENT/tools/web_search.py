
from ddgs import DDGS

from langchain.tools import tool
from pydantic import BaseModel, Field


class SearchInput(BaseModel):
    query: str = Field(
        description="The topic or question to search for on the web."
    )


@tool(args_schema=SearchInput)
def web_search(query: str) -> str:
    """
    Searches the internet for current information, articles,
    tutorials, technology updates, and other factual information.

    Use this tool when the user requests a web search or
    information that may have changed recently.
    """

    try:
        query = query.strip()

        if not query or len(query) > 300:
            return "Error: Please provide a valid search query."

        with DDGS() as ddgs:
            results = list(
                ddgs.text(
                    query,
                    max_results=5
                )
            )

        if not results:
            return "No search results were found."

        formatted_results = []

        for index, result in enumerate(results, start=1):
            formatted_results.append(
                f"""
Result {index}
Title: {result.get('title', 'No title')}
Description: {result.get('body', 'No description')}
URL: {result.get('href', 'No URL')}
"""
            )

        return "\n".join(formatted_results)

    except Exception:
        return (
            "Error: Web search is currently unavailable. "
            "Please try again later."
        )
 