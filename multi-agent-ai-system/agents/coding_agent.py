from utils.llm import ask_llm


def coding_agent(task, research):
    system_prompt = """
You are a Coding Agent in a Multi-Agent AI System.

Your job is to:
1. Analyze the technical requirements.
2. Design the programming solution.
3. Generate clean and maintainable code.
4. Explain important implementation decisions.
5. Follow modern programming practices.

Do not unnecessarily repeat the research.
Focus mainly on the technical implementation.
"""

    user_prompt = f"""
User Task:

{task}

Research Agent Notes:

{research}

Create the technical solution based on the above information.
"""

    return ask_llm(system_prompt, user_prompt)
