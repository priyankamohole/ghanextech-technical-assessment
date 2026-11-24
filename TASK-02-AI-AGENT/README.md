# Smart AI Assistant with Tool Calling

## Project Overview

Smart AI Assistant is an interactive AI-powered chatbot built using Python, Streamlit, LangChain, and Groq LLM. It can understand user queries, maintain conversational context, and dynamically select external tools to perform tasks.

Instead of generating every answer directly, the AI agent decides when to use tools such as a calculator, weather service, or web search to provide useful responses.

## Features

- Interactive chat interface built with Streamlit.
- Conversational memory to maintain chat context.
- Dynamic tool selection based on user queries.
- Calculator for mathematical operations.
- Weather tool for retrieving current weather information.
- Web search for retrieving relevant information from the internet.
- Error handling for failed tool executions.
- Modular and reusable project architecture.
- Environment variable configuration for API keys.

## Technology Stack

| Technology | Purpose                    |
| ---------- | -------------------------- |
| Python     | Backend development        |
| Streamlit  | User interface             |
| LangChain  | Agent and tool integration |
| LangGraph  | Conversation memory        |
| Groq API   | Large Language Model       |
| Pydantic   | Input validation           |
| Open-Meteo | Weather information        |
| DDGS       | Web search                 |
| Requests   | HTTP requests              |

## Available Tools

### 1. Calculator

- Performs mathematical calculations.
- Supports arithmetic operations and selected mathematical functions.
- Uses safe expression parsing instead of Python `eval()`.

### 2. Weather

- Retrieves current weather information for a specified city.
- Provides temperature, humidity, wind speed, and weather conditions.
- Uses the Open-Meteo API.

### 3. Web Search

- Searches the internet for relevant information.
- Returns search results with titles, descriptions, and links.
- Uses the DDGS library.

## Project Structure

```text
TASK-02-AI-AGENT/
│
├── app.py
├── requirements.txt
├── .env
├── .env.example
├── .gitignore
│
├── agent/
│   ├── __init__.py
│   └── agent.py
│
├── tools/
│   ├── __init__.py
│   ├── calculator.py
│   ├── weather.py
│   └── web_search.py
│
├── config/
│   ├── __init__.py
│   └── settings.py
│
└── utils/
    ├── __init__.py
    └── memory.py
```

## Agent Workflow

1. User enters a query through the Streamlit chat interface.
2. The query is passed to the LangChain AI agent.
3. The LLM analyzes the query and determines whether a tool is required.
4. The agent selects and executes the appropriate tool.
5. The tool returns its result to the agent.
6. The LLM generates a final response using the tool output.
7. Conversation history is maintained using LangGraph checkpointing.

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd TASK-02-AI-AGENT
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Linux/macOS**

```bash
source .venv/bin/activate
```

**Windows**

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
MODEL_NAME=openai/gpt-oss-20b
```

Get your API key from [Groq Console](https://console.groq.com/keys).

### 5. Run the application

```bash
streamlit run app.py
```

## Example Queries

- Calculate 250 multiplied by 40.
- What is the square root of 625?
- What is the current weather in Pune?
- Search for Python interview questions.
- Find the weather in Mumbai and calculate 20% of 1500.

## Deployment

The application can be deployed using Streamlit Community Cloud.

1. Push the project to a GitHub repository.
2. Open [Streamlit Community Cloud](https://share.streamlit.io/).
3. Connect your GitHub repository.
4. Select `app.py` as the main application file.
5. Add `GROQ_API_KEY` and `MODEL_NAME` under application secrets.
6. Deploy the application.

## Future Improvements

- Add more external tools and APIs.
- Support document-based question answering.
- Add persistent conversation storage.
- Improve tool execution monitoring.
- Add authentication and user-specific chat history.

## Author

Developed as a technical assessment project using Python, LangChain, Streamlit, and Groq.
