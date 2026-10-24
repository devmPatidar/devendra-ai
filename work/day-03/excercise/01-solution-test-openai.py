from openai import OpenAI
import json
from myprompts import MEDICAL_PROMPT

# Read API key from file
api_key_path = r"E:\Lenovo Ideapad 330\company-material\digital-workforce-transformation\ai-upskill-8\key-vault\openai\api.key"

with open(api_key_path, "r") as f:
    api_key = f.read().strip()

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Select model
MODEL = "gpt-3.5-turbo"


def build_prompt(user_query):

    # Prompt injection using formatted template
    prompt = f"""
SYSTEM:
You are a certified medical assistant
Answer only medical queries

TASK:
Answer the query in detail

CONSTRAINTS:
- No hallucination
- No diagnosis

OUTPUT:
{{
    "condition": "",
    "symptoms": [],
    "treatment": [],
    "confidence": "",
    "notes": ""
}}

USER QUERY:
{{{user_query}}}
"""
    
    # Use a named replacement to match templates that expect '{user_query}'
    prompt2 = MEDICAL_PROMPT.format(user_query=user_query, context=open("diabetes_context.txt").read() if open("diabetes_context.txt", "r") else "")

    return prompt2


def chat():

    print("\nMedical Assistant Powered by OpenAI")
    print("-" * 80)

    while True:

        # Get user input
        user_input = input("\nYou: ")

        # Exit condition
        if user_input.lower() in ["quit", "exit", "end"]:
            print("Goodbye!")
            break

        # Build the injected prompt
        final_prompt = build_prompt(user_input)

        # Show generated prompt (for debugging / learning)
        print("\n================ BUILT PROMPT ================\n")
        print(final_prompt)
        print("\n==============================================\n")

        try:

            # LLM call using Responses API
            response = client.responses.create(
                model=MODEL,
                input=final_prompt
            )

            # Extract model output
            ai_reply = response.output_text

            # Pretty print JSON if possible
            try:
                parsed_json = json.loads(ai_reply)

                print("AI Response:\n")
                print(json.dumps(parsed_json, indent=4))

            except Exception:
                print("AI:", ai_reply)

        except Exception as e:
            print("Inference failed with error:", e)


# Run app
if __name__ == "__main__":
    chat()