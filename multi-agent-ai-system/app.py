import streamlit as st

from agents.orchestrator import run_multi_agent_system


st.set_page_config(
    page_title="Multi-Agent AI System",
    page_icon="🤖",
    layout="wide"
)


st.title("🤖 Multi-Agent AI System")

st.markdown(
    """
### AI agents working together to solve complex tasks

This application uses multiple specialized AI agents:

- 🔎 Research Agent
- 💻 Coding Agent
- ✍️ Writer Agent
- 🧐 Review Agent
- 🎯 Orchestrator Agent
"""
)


st.divider()


task = st.text_area(
    "Enter your task",
    placeholder=(
        "Example: Create a Python expense tracker "
        "with SQLite database."
    ),
    height=150
)


if st.button("🚀 Run Multi-Agent System", type="primary"):

    if not task.strip():
        st.warning("Please enter a task first.")

    else:

        with st.spinner("AI agents are working together..."):

            try:

                result = run_multi_agent_system(task)

                st.success("Multi-Agent System completed successfully!")

                st.subheader("🎯 Final Answer")

                st.markdown(result["final"])

                with st.expander("🔎 Research Agent Output"):
                    st.markdown(result["research"])

                with st.expander("💻 Coding Agent Output"):
                    st.markdown(result["coding"])

                with st.expander("✍️ Writer Agent Draft"):
                    st.markdown(result["draft"])

            except Exception as error:

                st.error(
                    f"An error occurred: {error}"
                )


st.divider()

st.caption(
    "Multi-Agent AI System • Python • OpenAI API • Streamlit"
)
