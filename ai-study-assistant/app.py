```python
import streamlit as st
from openai import OpenAI

# -----------------------------
# PAGE CONFIGURATION
# -----------------------------
st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# TITLE
# -----------------------------
st.title("🤖 AI Study Assistant")
st.write("Your personal AI-powered learning assistant 📚")

st.divider()

# -----------------------------
# API KEY
# -----------------------------
api_key = st.text_input(
    "🔐 Enter your AI API Key",
    type="password",
    help="Your API key is used only for this session."
)

# -----------------------------
# SIDEBAR
# -----------------------------
with st.sidebar:
    st.header("📚 Study Tools")

    mode = st.selectbox(
        "Choose a mode",
        [
            "Ask AI",
            "Explain Topic",
            "Summarize Notes",
            "Generate MCQs"
        ]
    )

    st.divider()

    st.info(
        "💡 Tip: Ask clear questions to get better answers."
    )

# -----------------------------
# MAIN INPUT
# -----------------------------
if mode == "Ask AI":

    st.subheader("💬 Ask AI Anything")

    question = st.text_area(
        "Enter your question:",
        placeholder="Example: Explain Java OOP concepts in simple words."
    )

    if st.button("🚀 Ask AI"):

        if not api_key:
            st.warning("Please enter your API key first.")

        elif not question:
            st.warning("Please enter a question.")

        else:
            try:
                client = OpenAI(api_key=api_key)

                response = client.responses.create(
                    model="gpt-5-mini",
                    input=question
                )

                st.subheader("🤖 AI Answer")
                st.write(response.output_text)

            except Exception as e:
                st.error(f"Something went wrong: {e}")


# -----------------------------
# EXPLAIN TOPIC
# -----------------------------
elif mode == "Explain Topic":

    st.subheader("📖 Explain Any Topic")

    topic = st.text_input(
        "Enter a topic:",
        placeholder="Example: Machine Learning"
    )

    level = st.selectbox(
        "Choose your level",
        ["Beginner", "Intermediate", "Advanced"]
    )

    if st.button("📖 Explain"):

        if not api_key:
            st.warning("Please enter your API key first.")

        elif not topic:
            st.warning("Please enter a topic.")

        else:
            try:
                client = OpenAI(api_key=api_key)

                prompt = f"""
Explain the topic "{topic}" for a {level} student.

Include:
1. Simple definition
2. How it works
3. Real-world example
4. Important concepts
5. Simple example
6. Common interview questions
"""

                response = client.responses.create(
                    model="gpt-5-mini",
                    input=prompt
                )

                st.subheader("📚 Explanation")
                st.write(response.output_text)

            except Exception as e:
                st.error(f"Something went wrong: {e}")


# -----------------------------
# SUMMARIZE NOTES
# -----------------------------
elif mode == "Summarize Notes":

    st.subheader("📝 Summarize Your Notes")

    notes = st.text_area(
        "Paste your notes here:",
        height=250,
        placeholder="Paste your study notes..."
    )

    if st.button("✨ Summarize"):

        if not api_key:
            st.warning("Please enter your API key first.")

        elif not notes:
            st.warning("Please paste some notes.")

        else:
            try:
                client = OpenAI(api_key=api_key)

                prompt = f"""
Summarize the following study notes.

Make the summary:
- Simple
- Clear
- Well structured
- Easy to remember

Also provide:
1. Key points
2. Important terms
3. Quick revision notes

NOTES:

{notes}
"""

                response = client.responses.create(
                    model="gpt-5-mini",
                    input=prompt
                )

                st.subheader("✨ Summary")
                st.write(response.output_text)

            except Exception as e:
                st.error(f"Something went wrong: {e}")


# -----------------------------
# GENERATE MCQs
# -----------------------------
elif mode == "Generate MCQs":

    st.subheader("❓ AI MCQ Generator")

    topic = st.text_input(
        "Enter a topic:",
        placeholder="Example: SQL Joins"
    )

    number = st.slider(
        "Number of questions",
        min_value=1,
        max_value=10,
        value=5
    )

    if st.button("🎯 Generate MCQs"):

        if not api_key:
            st.warning("Please enter your API key first.")

        elif not topic:
            st.warning("Please enter a topic.")

        else:
            try:
                client = OpenAI(api_key=api_key)

                prompt = f"""
Create {number} multiple-choice questions about "{topic}".

For each question provide:

Question:
A)
B)
C)
D)

Correct Answer:
Explanation:

Make the questions suitable for students.
"""

                response = client.responses.create(
                    model="gpt-5-mini",
                    input=prompt
                )

                st.subheader("🎯 Generated MCQs")
                st.write(response.output_text)

            except Exception as e:
                st.error(f"Something went wrong: {e}")


# -----------------------------
# FOOTER
# -----------------------------
st.divider()

st.caption(
    "🤖 AI Study Assistant | Built with Python + Streamlit + AI API"
)
```
