from openai import OpenAI

with open(r"C:\Users\user\Desktop\devendra-ai\work\key-vault\openrouter\openrouter-api.key") as f:
    api_key = f.read().strip()


client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)




response = client.chat.completions.create(
    model="qwen/qwen-2.5-72b-instruct",
    messages=[
        {
            "role": "system",
            "content": (
                "You are an expert in Agentic AI, banking, "
                "financial services, and enterprise AI architecture."
            ),
        },
        {
            "role": "user",
            "content": (
                "Explain 2 practical Agentic AI use cases in banking. "
                "For each use case, include the business problem, "
                "how the AI agent works, tools and systems it uses, "
                "business benefits, and risks or controls required."
            ),
        },
    ],
    temperature=0.3,
    max_tokens=1000,
)

print(response.choices[0].message.content)