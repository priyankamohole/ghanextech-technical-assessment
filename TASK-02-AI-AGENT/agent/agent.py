
from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langgraph.checkpoint.memory import InMemorySaver

from config.settings import (
    GROQ_API_KEY,
    MODEL_NAME,
    validate_settings
)

from tools.calculator import calculator
from tools.weather import get_weather
from tools.web_search import web_search


SYSTEM_PROMPT = """
You are a helpful and intelligent AI assistant.

Your job is to answer user questions and use tools whenever needed.

AVAILABLE TOOLS:

1. calculator:
   Use for mathematical calculations.

2. get_weather:
   Use for current weather information about a city.

3. web_search:
   Use for internet searches and information that may
   be current or require external sources.

INSTRUCTIONS:

- Understand the user's intent before responding.
- Use tools only when necessary.
- Do not use tools for greetings or simple conversational queries.
- You can use multiple tools when the request requires them.
- Never invent tool results.
- If a tool returns an error, explain the problem politely.
- Use the actual tool output when generating your response.
- Keep responses clear, friendly, and well structured.
- Remember previous messages in the same conversation.
- Ask a clarifying question when essential information is missing.
"""


def create_ai_agent():

    validate_settings()

    llm = ChatGroq(
        model=MODEL_NAME,
        temperature=0,
        api_key=GROQ_API_KEY
    )

    tools = [
        calculator,
        get_weather,
        web_search
    ]

    memory = InMemorySaver()

    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=SYSTEM_PROMPT,
        checkpointer=memory
    )

    return agent
    