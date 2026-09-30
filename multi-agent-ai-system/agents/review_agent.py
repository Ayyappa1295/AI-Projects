from utils.llm import ask_llm


def review_agent(task, draft):
    system_prompt = """
You are a Review Agent in a Multi-Agent AI System.

Your job is to review the generated answer.

Check for:
1. Technical mistakes.
2. Missing information.
3. Incorrect assumptions.
4. Poor structure.
5. Unnecessary repetition.
6. Code problems.
7. Clarity.

After reviewing, produce an improved final answer.

Do not talk about the internal agent workflow unless it is useful.
"""

    user_prompt = f"""
Original User Task:

{task}

Generated Draft:

{draft}

Review and improve the draft.

Return ONLY the final improved answer.
"""

    return ask_llm(system_prompt, user_prompt)
