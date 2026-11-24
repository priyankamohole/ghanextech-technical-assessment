
import streamlit as st

from agent.agent import create_ai_agent
from utils.memory import create_thread_id



GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
SERPER_API_KEY = st.secrets["SERPER_API_KEY"]
GROQ_MODEL = st.secrets["GROQ_MODEL"]


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Smart AI Assistant",
    page_icon="🤖",
    layout="wide"
)


# ---------------- CUSTOM STYLING ----------------

st.markdown("""
<style>
    .main-title {
        font-size: 35px;
        font-weight: 700;
        text-align: center;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: gray;
        margin-bottom: 30px;
    }

    .stChatMessage {
        border-radius: 12px;
    }
</style>
""", unsafe_allow_html=True)


# ---------------- AGENT INITIALIZATION ----------------

@st.cache_resource
def load_agent():
    return create_ai_agent()


if "messages" not in st.session_state:
    st.session_state.messages = []

if "thread_id" not in st.session_state:
    st.session_state.thread_id = create_thread_id()

if "agent" not in st.session_state:
    try:
        st.session_state.agent = load_agent()
    except Exception as e:
        st.error(f"Agent initialization failed: {e}")
        st.stop()


# ---------------- HEADER ----------------

st.markdown(
    '<div class="main-title">🤖 Smart AI Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'An intelligent assistant powered by Groq and LangChain'
    '</div>',
    unsafe_allow_html=True
)


# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.title("⚙️ Assistant Settings")

    st.success("Agent is ready")

    st.markdown("### Available Tools")

    st.markdown("""
    - 🧮 Calculator
    - 🌤️ Weather Information
    - 🔎 Web Search
    """)

    st.divider()

    st.markdown("### Example Questions")

    examples = [
        "Calculate 250 * 45",
        "What is the weather in Pune?",
        "Search for Python interview questions",
        "Explain artificial intelligence",
        "Find the weather in Mumbai and calculate 25% of 800"
    ]

    for example in examples:
        st.caption(f"• {example}")

    st.divider()

    if st.button("🗑️ Clear Conversation", use_container_width=True):

        st.session_state.messages = []
        st.session_state.thread_id = create_thread_id()

        st.rerun()


# ---------------- CHAT HISTORY ----------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# ---------------- CHAT INPUT ----------------

prompt = st.chat_input("Ask me anything...")


if prompt:

    # Display user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI response
    with st.chat_message("assistant"):

        with st.spinner("Thinking and selecting tools..."):

            try:

                response = st.session_state.agent.invoke(
                    {
                        "messages": [
                            {
                                "role": "user",
                                "content": prompt
                            }
                        ]
                    },
                    config={
                        "configurable": {
                            "thread_id": st.session_state.thread_id
                        }
                    }
                )

                result_messages = response["messages"]

                # Display tool execution information
                tool_calls = []
                tool_results = []

                for message in result_messages:

                    if getattr(message, "tool_calls", None):
                        tool_calls.extend(message.tool_calls)

                    if getattr(message, "type", None) == "tool":
                        tool_results.append(message)

                if tool_calls:
                    with st.expander("🔧 Agent tool activity"):
                        for call in tool_calls:
                            st.write(
                                f"**Tool:** {call.get('name')}"
                            )
                            st.json(call.get("args", {}))

                        for tool_result in tool_results:
                            st.write(
                                f"**{tool_result.name} result:**"
                            )
                            st.write(tool_result.content)

                # Extract final AI response
                ai_messages = [
                    msg for msg in result_messages
                    if getattr(msg, "type", None) == "ai"
                    and msg.content
                    and not getattr(msg, "tool_calls", None)
                ]

                if not ai_messages:
                    raise RuntimeError(
                        "The agent did not generate a final response."
                    )

                answer = ai_messages[-1].content

                # Handle text-block responses
                if isinstance(answer, list):
                    answer = "\n".join(
                        str(block.get("text", block))
                        if isinstance(block, dict)
                        else str(block)
                        for block in answer
                    )

                st.markdown(answer)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer
                })

            except Exception as e:

                error_message = (
                    "Sorry, something went wrong while processing "
                    "your request. Please try again.\n\n"
                    f"Details: {str(e)[:300]}"
                )

                st.error(error_message)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": error_message
                })
