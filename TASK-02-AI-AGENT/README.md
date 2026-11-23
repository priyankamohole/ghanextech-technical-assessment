# 🤖 Smart AI Assistant with Tool Calling

An intelligent conversational AI agent built using Python,
LangChain, Groq and Streamlit.

The agent understands user queries and dynamically invokes
external tools to perform calculations, retrieve live weather
information and search the web.

## Features

- Conversational chat interface
- Multi-turn conversation memory
- LLM-based tool selection
- Calculator tool
- Real-time weather tool
- Web search tool
- Multiple tool execution
- Structured tool input schemas
- Exception handling
- Interactive Streamlit interface

## Technology Stack

- Python
- Streamlit
- LangChain
- LangGraph
- Groq LLM
- Open-Meteo API
- DuckDuckGo Search
- Pydantic
- Requests

## Architecture

User Query
|
v
Streamlit Interface
|
v
LangChain AI Agent
|
v
LLM Intent Analysis
|
+---- Direct Response
|
+---- Calculator Tool
|
+---- Weather Tool
|
+---- Web Search Tool
|
v
Tool Execution
|
v
LLM Response Synthesis
|
v
Final Response

## Tools

### 1. Calculator

Performs safe mathematical calculations.

Input:

- expression: string

### 2. Weather

Fetches current weather information using Open-Meteo.

Input:

- city: string

### 3. Web Search

Searches the internet using DuckDuckGo.

Input:

- query: string

## Example Prompts

Direct response:

- Hello!
- Explain artificial intelligence.

Calculator:

- Calculate 450 \* 25.
- What is the square root of 625?

Weather:

- What is the weather in Pune?

Web Search:

- Search for Python interview questions.

Multiple tools:

- Find the weather in Pune and calculate
  25% of 800.

## Installation

1. Clone the repository.

git clone YOUR_GITHUB_REPOSITORY_URL

2. Navigate to the project.

cd ai-tool-calling-agent

3. Create a virtual environment.

python -m venv .venv

4. Activate the environment.

Linux/Mac:
source .venv/bin/activate

Windows:
.venv\Scripts\activate

5. Install dependencies.

pip install -r requirements.txt

6. Configure environment variables.

Create a .env file and add:

GROQ_API_KEY=your_groq_api_key
MODEL_NAME=openai/gpt-oss-20b

7. Start the application.

streamlit run app.py

## Deployment

The application can be deployed using
Streamlit Community Cloud.

Connect your GitHub repository and configure
GROQ_API_KEY in the application's secrets.

## Future Improvements

- Persistent conversation database
- More external API integrations
- Voice-based interaction
- User authentication
- Advanced agent monitoring
- Streaming responses

## Author

Developed as an AI Agent with Tool Calling assignment.
