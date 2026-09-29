import os
from dotenv import load_dotenv
import streamlit as st
from openai import OpenAI

# --------------------------------------------------
# Load environment variables
# --------------------------------------------------

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# --------------------------------------------------
# Custom CSS
# --------------------------------------------------

st.markdown(
    """
    <style>

    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #777;
        font-size: 17px;
        margin-bottom: 30px;
    }

    .feature-box {
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #ddd;
        margin-bottom: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# Header
# --------------------------------------------------

st.markdown(
    '<div class="main-title">🤖 AI Chatbot</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Your intelligent AI-powered virtual assistant</div>',
    unsafe_allow_html=True
)

# --------------------------------------------------
# API Key Check
# --------------------------------------------------

if not API_KEY:

    st.error(
        "OpenAI API key not found. Please add OPENAI_API_KEY to your .env file."
    )

    st.stop()

# --------------------------------------------------
# OpenAI Client
# --------------------------------------------------

client = OpenAI(api_key=API_KEY)

# --------------------------------------------------
# Session State
# --------------------------------------------------

if "messages" not in st.session_state:

    st.session_state.messages = [
        {
            "role": "system",
            "content": """
You are a helpful, friendly and intelligent AI assistant.

Your responsibilities:

1. Answer questions clearly.
2. Explain difficult topics in simple language.
3. Help with programming and technology.
4. Help students with learning.
5. Provide examples whenever useful.
6. If the user asks for code, provide clean and understandable code.
7. Be polite and conversational.
8. If you do not know something, clearly say so.
9. Never invent facts.
"""
        }
    ]

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:

    st.header("⚙️ Chat Settings")

    st.write("### 🤖 AI Assistant")

    st.info(
        "Ask questions about programming, AI, technology, education, "
        "or general topics."
    )

    if st.button("🗑️ Clear Chat", use_container_width=True):

        st.session_state.messages = [
            {
                "role": "system",
                "content": """
You are a helpful, friendly and intelligent AI assistant.

Answer questions clearly and provide useful examples.
"""
            }
        ]

        st.rerun()

    st.divider()

    st.write("### ✨ Features")

    st.write("✅ AI-powered responses")
    st.write("✅ Conversation memory")
    st.write("✅ Real-time chat")
    st.write("✅ Clear conversation")
    st.write("✅ Secure API key")
    st.write("✅ Student-friendly assistant")

# --------------------------------------------------
# Display Chat History
# --------------------------------------------------

for message in st.session_state.messages:

    if message["role"] == "system":
        continue

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# --------------------------------------------------
# Chat Input
# --------------------------------------------------

user_input = st.chat_input(
    "💬 Ask me anything..."
)

# --------------------------------------------------
# Generate AI Response
# --------------------------------------------------

if user_input:

    # Display user message

    with st.chat_message("user"):

        st.markdown(user_input)

    # Store user message

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Generate response

    with st.chat_message("assistant"):

        response_placeholder = st.empty()

        try:

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=st.session_state.messages,
                temperature=0.7
            )

            assistant_response = response.choices[0].message.content

            response_placeholder.markdown(assistant_response)

            # Store AI response

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": assistant_response
                }
            )

        except Exception as error:

            error_message = (
                "❌ Something went wrong.\n\n"
                "Please check your API key, internet connection, "
                "and API account settings."
            )

            response_placeholder.error(error_message)

            print(error)

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.divider()

st.caption(
    "🤖 AI Chatbot | Built with Python, Streamlit & OpenAI API"
)
