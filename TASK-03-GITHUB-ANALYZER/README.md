# 🔍 RepoInsight-AI

### AI-Powered GitHub Repository Analyzer

RepoInsight-AI is an AI-powered GitHub repository analysis application built using Python, Streamlit, GitHub REST API, and Groq LLM.

It helps developers understand unfamiliar GitHub repositories by extracting repository metadata, analyzing README documentation, identifying programming languages and technologies, examining project structure, and generating AI-powered insights.

The application provides an interactive dashboard with repository information, architecture analysis, project strengths, actionable recommendations, and potential open-source contribution opportunities.

---

## 🚀 Features

- **GitHub Repository Analysis:** Analyze public repositories using a GitHub URL or `owner/repository` format.
- **Repository Metadata Extraction:** Retrieve repository name, description, stars, forks, license, and other information.
- **README Analysis:** Extract and analyze repository documentation.
- **Technology Stack Detection:** Identify programming languages and technologies using GitHub language statistics and package configuration files.
- **Directory Structure Analysis:** Retrieve repository files and directory information.
- **AI-Powered Analysis:** Use Groq LLM to generate structured repository insights.
- **Architecture Analysis:** Understand the repository's architecture and code organization based on collected evidence.
- **Project Strengths:** Identify important project characteristics and strengths.
- **Actionable Recommendations:** Generate at least three improvement recommendations with priority levels and supporting evidence.
- **Contribution Opportunities:** Discover potential areas for open-source contributions.
- **Interactive Dashboard:** Display repository metrics and AI-generated insights using Streamlit.

---

## 🛠️ Technology Stack

| Technology      | Purpose                          |
| --------------- | -------------------------------- |
| Python          | Core application development     |
| Streamlit       | Interactive web application      |
| GitHub REST API | Repository data extraction       |
| Groq API        | Large Language Model integration |
| Pydantic        | Structured response validation   |
| Requests        | HTTP communication               |
| Plotly          | Data visualization               |
| python-dotenv   | Environment variable management  |

---

## 📁 Project Structure

```text
TASK-03-GITHUB-ANALYZER/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
│
├── config/
│   ├── __init__.py
│   └── settings.py
│
├── services/
│   ├── __init__.py
│   ├── github_client.py
│   ├── llm_service.py
│   ├── prompt_templates.py
│   └── repository_analyzer.py
│
├── utils/
│   ├── __init__.py
│   └── validators.py
│
└── tests/
    ├── __init__.py
    ├── test_ai_analysis.py
    └── test_github_client.py
```

---

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/TASK-03-GITHUB-ANALYZER.git

cd TASK-03-GITHUB-ANALYZER
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create a virtual environment

**Linux / macOS**

```bash
python3 -m venv .venv

source .venv/bin/activate
```

**Windows**

```bash
python -m venv .venv

.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
GITHUB_TOKEN=your_github_token
GROQ_MODEL=openai/gpt-oss-120b
```

**Get your API keys:**

- Groq API: https://console.groq.com/keys
- GitHub Personal Access Token: https://github.com/settings/tokens

Note:

- GitHub token authentication is optional for public repositories.
- Using a GitHub token helps increase API rate limits.
- Never expose your API keys or commit your `.env` file to GitHub.

### 5. Run the application

```bash
streamlit run app.py
```

Open the URL displayed in your terminal:

```text
http://localhost:8501
```

---

## 💻 How to Use

1. Launch the Streamlit application.
2. Enter a public GitHub repository URL.
3. Click the **Analyze Repository** button.
4. The application validates the repository URL.
5. GitHub REST API fetches repository metadata, README, languages, directory structure, and package files.
6. The collected information is passed to the Groq LLM.
7. The AI generates structured repository insights.
8. Pydantic validates the generated response.
9. Explore the analysis through the Streamlit dashboard.

### Example repositories

You can test the application using these public repositories:

| Repository | URL                                       |
| ---------- | ----------------------------------------- |
| FastAPI    | https://github.com/fastapi/fastapi        |
| Flask      | https://github.com/pallets/flask          |
| React      | https://github.com/facebook/react         |
| Django     | https://github.com/django/django          |
| LangChain  | https://github.com/langchain-ai/langchain |

---

## 🧠 AI Analysis

The application generates the following insights:

### 1. Executive Summary

Provides an overview of the repository, its purpose, technologies, and ecosystem.

### 2. Technology Stack

Identifies programming languages, frameworks, and development tools using repository evidence.

### 3. Project Strengths

Highlights positive aspects such as documentation, community adoption, and technology choices.

### 4. Architecture Analysis

Examines project organization, architecture style, and important structural observations.

### 5. AI Recommendations

Generates actionable recommendations containing:

- Recommendation title
- Identified problem
- Suggested solution
- Priority level (High, Medium, Low)
- Supporting evidence

### 6. Contribution Opportunities

Identifies potential areas where developers can contribute through code improvements, documentation, testing, and other enhancements.

---

## 🧪 Testing

Run the GitHub API integration test:

```bash
python -m tests.test_github_client
```

Run the complete AI analysis test:

```bash
python -m tests.test_ai_analysis
```

Run tests from the project root directory.

---

## 🔐 Error Handling

The application handles common errors, including:

- Invalid GitHub repository URLs
- Repositories that do not exist or cannot be accessed
- GitHub API rate limits
- Network connection failures
- Missing API configuration
- Invalid or incomplete AI-generated responses
- Pydantic response validation errors

---

## ⚠️ Limitations

- Currently designed primarily for public GitHub repositories.
- Analysis quality depends on the repository information successfully retrieved.
- Large repositories may have truncated directory information.
- AI recommendations are suggestions and should be reviewed by developers.
- Limited repository evidence may lead to incomplete architectural conclusions.
- Groq API usage is subject to model availability and account rate limits.

---

## 🔮 Future Enhancements

- Modular Streamlit dashboard components.
- Deeper source-code analysis.
- Repository comparison functionality.
- Automated GitHub issue and pull request analysis.
- Code quality and security analysis.
- Downloadable PDF analysis reports.
- Repository analysis history and caching.
- Evidence-based recommendation confidence scoring.
- Open-source contribution workflow assistance.

---

## 👩‍💻 Author

**Priyanka Mohole**

GitHub: https://github.com/priyankamohole

---

## 📄 License

This project is currently an educational and development project.

A license for RepoInsight-AI has not yet been specified. Add a suitable `LICENSE` file before distributing it as an open-source project.
