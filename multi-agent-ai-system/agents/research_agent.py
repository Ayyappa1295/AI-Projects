from utils.llm import ask_llm


def research_agent(task):
    system_prompt = """
You are a Research Agent in a Multi-Agent AI System.

Your job is to:
1. Understand the user's task.
2. Identify important concepts.
3. Break the problem into useful research areas.
4. Provide accurate technical information.
5. Give useful recommendations to other agents.

Do not write the final answer.
Return structured research notes.
"""

    user_prompt = f"""
User Task:

{task}

Prepare detailed research notes that can be used by the other AI agents.
"""

    return ask_llm(system_prompt, user_prompt)
