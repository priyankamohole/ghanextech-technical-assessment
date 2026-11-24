
from services.github_client import GitHubClient
from services.llm_service import LLMService
from utils.validators import validate_github_repo


def test_ai_analysis():

    repo_url = "https://github.com/streamlit/streamlit"

    owner, repo = validate_github_repo(repo_url)

    print("Fetching repository information...")

    github = GitHubClient()

    repository_data = github.analyze_repository(
        owner,
        repo
    )

    print("Repository data collected!")

    print("Starting AI analysis...")

    llm = LLMService()

    analysis = llm.analyze_repository(
        repository_data
    )

    print("\n========== EXECUTIVE SUMMARY ==========")

    print(analysis.executive_summary)

    print("\n========== TECHNOLOGIES ==========")

    for technology in analysis.technologies:
        print(
            technology.name,
            "|",
            technology.category,
            "|",
            technology.evidence
        )

    print("\n========== STRENGTHS ==========")

    for strength in analysis.strengths:
        print("-", strength)

    print("\n========== ARCHITECTURE ==========")

    print(analysis.architecture.model_dump_json(indent=2))

    print("\n========== RECOMMENDATIONS ==========")

    for recommendation in analysis.recommendations:

        print("\nTitle:", recommendation.title)
        print("Problem:", recommendation.problem)
        print("Solution:", recommendation.suggested_solution)
        print("Priority:", recommendation.priority)
        print("Evidence:", recommendation.evidence)

    print("\n========== CONTRIBUTION OPPORTUNITIES ==========")

    for opportunity in analysis.contribution_opportunities:

        print("\nArea:", opportunity.area)
        print("Opportunity:", opportunity.opportunity)
        print("Reason:", opportunity.rationale)

    print("\nAI analysis completed successfully!")


if __name__ == "__main__":
    test_ai_analysis()
