# Internship Assessment Submission - Priyanka Raju Mohole

## Candidate Information

- **Full Name:** Priyanka Raju Mohole
- **Email Address:** priyankamohole@gmail.com
- **GitHub Profile URL:** https://github.com/priyankamohole
- **LinkedIn Profile:** https://www.linkedin.com/in/priyanka-mohole-626366250/
- **Submission Date:** 24 November 2026

---

## Task Deliverables

### Task 1: AI Document Assistant (RAG)

- **GitHub Repository URL:** [Your Task 1 repository URL]
- **Live Deployed Application URL:** https://document-assistant-rag.streamlit.app/
- **Primary Technologies Used:** Python, Streamlit, LangChain, Hugging Face Embeddings, FAISS, Groq API.

- **Project Summary:**

  Developed an AI-powered document assistant using Retrieval-Augmented Generation (RAG). The application processes uploaded PDF documents, extracts their text, splits the content into smaller chunks, and generates embeddings using a sentence-transformer embedding model.

  The generated embeddings are stored in a FAISS vector database. When a user asks a question, the application retrieves relevant document chunks and uses a language model through the Groq API to generate a context-based response. The application provides an interactive Streamlit interface for document upload and question answering.

- **Key Challenges & Solutions:**

  Faced challenges with embedding model initialization, document processing, and integrating the retrieval pipeline with the language model. Addressed these issues by configuring the embedding model correctly, organizing the document-processing workflow, and debugging LangChain integration errors.

---

### Task 2: AI Agent with Tool Calling

- **GitHub Repository URL:** https://github.com/priyankamohole/Smart-AI-Assistant-with-Tool-Calling
- **Live Deployed Application URL:** https://smart-ai-assistant-tool.streamlit.app/
- **Primary Technologies Used:** Python, Streamlit, LangChain, LangGraph, Groq API, DuckDuckGo Search, Open-Meteo API.

- **Implemented Tools:**
  1. **Calculator:** Performs mathematical calculations based on user-provided expressions.
  2. **Weather Tool:** Retrieves weather information for a specified location.
  3. **Web Search:** Searches the web using DuckDuckGo to retrieve relevant information.

- **Project Summary:**

  Developed an AI assistant using LangChain's agent framework and a Groq-powered language model. The agent receives user queries, determines whether a registered tool is required, executes the appropriate tool, and uses the returned results to formulate a response.

  Integrated calculator, weather, and web-search tools to support different types of user queries. Used LangGraph's InMemorySaver for conversation checkpointing and Streamlit to create an interactive chat interface. Added configuration management for API credentials using environment variables and Streamlit Secrets.

- **Key Challenges & Solutions:**

  Encountered dependency installation issues, tool integration errors, and deployment configuration problems. Resolved these by adding the required dependencies, debugging tool implementations, configuring Streamlit Secrets, and separating application settings from agent logic.

---

### Task 3: GitHub Repository AI Analyzer & Open-Source Contribution

- **GitHub Repository URL:** [Your Task 3 repository URL]
- **Live Deployed Application URL:** https://repoinsight-ai-assistant.streamlit.app/
- **Primary Technologies Used:** Python, Streamlit, GitHub REST API, [Your AI model/API].

- **Project Summary:**

  Developed RepoInsight-AI, a tool designed to analyze GitHub repositories. The application accepts a GitHub repository URL and retrieves repository information using the GitHub API.

  It analyzes repository metadata and available development metrics, then presents the collected information through an interactive interface. AI-powered analysis can be used to generate insights and recommendations based on the retrieved repository information.

- **Key Challenges & Solutions:**

Faced challenges with GitHub API integration, repository URL validation, and extracting meaningful repository metrics. Resolved them by implementing API requests, validating user inputs, processing repository data, and handling errors. Also structured repository information to generate useful AI-powered insights and recommendations.

-### Open-Source Contribution

- **Target Open-Source Repository:** Pending
- **Contribution URL (Issue / Pull Request):** Pending
- **Contribution Summary:**

  I am currently exploring open-source projects to identify an improvement opportunity. I plan to contribute by fixing a minor bug, improving documentation, or enhancing an existing feature. I will include the public Issue or Pull Request URL after submitting my contribution.

## AI Collaboration Disclosure

- **AI Tools Used:** ChatGPT
- **How You Leveraged AI:** Used AI tools to understand technical concepts, plan project architecture, generate implementation ideas, debug errors, understand API integration, and improve documentation.
- **Verification & Ownership:**

  Reviewed and tested the implemented code, verified application functionality, and worked through development and deployment issues. Used AI assistance as a development aid while taking responsibility for understanding, validating, and maintaining the submitted implementation.

---
