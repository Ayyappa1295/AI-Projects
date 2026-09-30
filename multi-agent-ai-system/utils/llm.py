from openai import OpenAI
from config.settings import OPENAI_API_KEY, MODEL_NAME

if not OPENAI_API_KEY:
    raise ValueError(
        "OPENAI_API_KEY is missing. Please create a .env file "
        "and add your OpenAI API key."
    )

client = OpenAI(api_key=OPENAI_API_KEY)


def ask_llm(system_prompt, user_prompt):
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content
