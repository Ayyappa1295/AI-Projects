from agents.research_agent import research_agent
from agents.coding_agent import coding_agent
from agents.writer_agent import writer_agent
from agents.review_agent import review_agent


def run_multi_agent_system(task):

    # Step 1: Research
    research = research_agent(task)

    # Step 2: Coding / Technical Solution
    coding = coding_agent(task, research)

    # Step 3: Writing
    draft = writer_agent(
        task,
        research,
        coding
    )

    # Step 4: Review
    final_answer = review_agent(
        task,
        draft
    )

    return {
        "research": research,
        "coding": coding,
        "draft": draft,
        "final": final_answer
    }
