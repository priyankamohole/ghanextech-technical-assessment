
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

def get_setting(key, default=None):
    """Read configuration from Streamlit Secrets or local environment."""

    try:
        value = st.secrets.get(key)
        if value:
            return value
    except Exception:
        pass

    return os.getenv(key, default)

GROQ_API_KEY = get_setting("GROQ_API_KEY")

MODEL_NAME = get_setting(
    "GROQ_MODEL",
    "openai/gpt-oss-20b"
)


# GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
# GROQ_MODEL = st.secrets["GROQ_MODEL"]


def validate_settings():
    if not GROQ_API_KEY:
        raise ValueError(
            "GROQ_API_KEY is missing. "
            "Please configure it in your .env file."
        )
