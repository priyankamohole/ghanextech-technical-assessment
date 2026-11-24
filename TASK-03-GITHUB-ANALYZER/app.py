
import streamlit as st
import plotly.express as px

from services.github_client import GitHubClient, GitHubAPIError
from services.llm_service import LLMService
from utils.validators import validate_github_repo

st.set_page_config(
    page_title="GitHub AI Analyzer",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 GitHub Repository AI Analyzer")
st.caption(
    "Analyze GitHub repositories using GitHub REST API and AI."
)

repo_input = st.text_input(
    "GitHub Repository URL",
    placeholder="https://github.com/streamlit/streamlit"
)

analyze_button = st.button(
    "🚀 Analyze Repository",
    type="primary",
    use_container_width=True
)

if analyze_button:

    if not repo_input.strip():
        st.warning("Please enter a GitHub repository URL.")

    else:
        try:
            owner, repo = validate_github_repo(repo_input)

            with st.spinner("Fetching repository information..."):
                github = GitHubClient()
                repository_data = github.analyze_repository(
                    owner, repo
                )

            with st.spinner("AI is analyzing the repository..."):
                llm = LLMService()
                analysis = llm.analyze_repository(
                    repository_data
                )

            metadata = repository_data["metadata"]

            st.success("Repository analysis completed!")

            # Repository overview
            st.header("📊 Repository Overview")

            col1, col2, col3, col4 = st.columns(4)

            col1.metric(
                "⭐ Stars",
                f"{metadata.get('stargazers_count', 0):,}"
            )

            col2.metric(
                "🍴 Forks",
                f"{metadata.get('forks_count', 0):,}"
            )

            col3.metric(
                "🐛 Open Issues / PRs",
                f"{metadata.get('open_issues_count', 0):,}"
            )

            col4.metric(
                "💻 Primary Language",
                metadata.get("language") or "Unknown"
            )

            st.markdown("---")

            # Executive summary
            st.header("📝 Executive Summary")
            st.write(analysis.executive_summary)

            # Technology distribution
            st.header("🛠️ Technology Stack")

            languages = repository_data.get("languages", {})

            if languages:
                language_df = {
                    "Language": list(languages.keys()),
                    "Bytes": list(languages.values())
                }

                fig = px.pie(
                    language_df,
                    names="Language",
                    values="Bytes",
                    title="Programming Language Distribution",
                    hole=0.4
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

            for technology in analysis.technologies:
                st.markdown(
                    f"- **{technology.name}** "
                    f"({technology.category}) — "
                    f"{technology.evidence}"
                )

            st.markdown("---")

            # Strengths
            st.header("💪 Project Strengths")

            for strength in analysis.strengths:
                st.markdown(f"- {strength}")

            # Architecture
            st.header("🏗️ Architecture Analysis")

            st.subheader(
                analysis.architecture.architecture_style
            )

            st.write(
                analysis.architecture.code_organization
            )

            for observation in (
                analysis.architecture.important_observations
            ):
                st.markdown(f"- {observation}")

            st.markdown("---")

            # Recommendations
            st.header("💡 AI Recommendations")

            for index, recommendation in enumerate(
                analysis.recommendations, start=1
            ):
                with st.expander(
                    f"{index}. {recommendation.title} "
                    f"({recommendation.priority})"
                ):
                    st.write("**Problem**")
                    st.write(recommendation.problem)

                    st.write("**Suggested Solution**")
                    st.write(recommendation.suggested_solution)

                    st.write("**Evidence**")
                    st.write(recommendation.evidence)

            # Contribution opportunities
            st.header("🤝 Contribution Opportunities")

            for opportunity in (
                analysis.contribution_opportunities
            ):
                with st.expander(opportunity.area):
                    st.write(opportunity.opportunity)
                    st.caption(opportunity.rationale)

            # Limitations
            if analysis.analysis_limitations:
                st.header("⚠️ Analysis Limitations")

                for limitation in analysis.analysis_limitations:
                    st.warning(limitation)

            # Repository links
            st.markdown("---")
            st.subheader("🔗 Repository Links")

            st.markdown(
                f"[Open GitHub Repository]"
                f"(https://github.com/{owner}/{repo})"
            )

        except ValueError as error:
            st.error(str(error))

        except GitHubAPIError as error:
            st.error(f"GitHub API Error: {error}")

        except Exception as error:
            st.error(f"Analysis failed: {error}")
            st.exception(error)
