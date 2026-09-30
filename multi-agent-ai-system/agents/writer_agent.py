from utils.llm import ask_llm


def writer_agent(task, research, coding):
    system_prompt = """
You are a Technical Writer Agent.

Your job is to convert research and technical work into a clear,
professional response.

The final response should:
- Have clear headings.
- Be easy to understand.
- Explain important concepts.
- Include relevant code when needed.
- Avoid unnecessary repetition.
"""

    user_prompt = f"""
User Task:

{task}

Research:

{research}

Coding Solution:

{coding}

Create a professional draft response for the user.
"""

    return ask_llm(system_prompt, user_prompt)
