# Imports
from groq import Groq


# Read API key
with open(r"C:\Users\user\Desktop\devendra-ai\work\key-vault\groq\groq-api.key", encoding="utf-8") as key_file:
    GROQ_API_KEY = key_file.read().strip()

# Initialize Groq client
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is not set. Please add it to your environment or .env file.")
client = Groq(api_key=GROQ_API_KEY)

# Select model
MODEL_NAME = "openai/gpt-oss-20b"   # Example model available on Groq

# Chat function
def chat():

    # Welcome message
    print("Welcome to the Groq chatbot! Type 'exit', 'quit', or 'end' to stop.")

    # Conversation history (list)
    conversation_history = [{"role": "system","content": "Only answer physics-related questions. For other questions, politely say you can only help with physics."}]

    # Inifinite loop
    while True:

        # User input
        user_input = input("You: ").strip()

        # Check for the exit condition (exit, quit, end)
        if user_input.lower() in {"exit", "quit", "end"}:
            print("Goodbye!")
            break

        # Add user input to conversation history
        conversation_history.append({"role": "user", "content": user_input})

        # Build a prompt using conversation history
        try:

            # Get the Groq response
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=conversation_history,
                temperature=0.7,
                max_tokens=512,
            )

            # extract the output text
            ai_message = response.choices[0].message.content

            # print the output text
            print(f"Bot: {ai_message}")

            # add the ai message into the conversation history as an object with a role
            conversation_history.append({"role": "assistant", "content": ai_message})

        except Exception as e:

            # Add an exception message
            error_message = f"Error: {str(e)}"
            print(error_message)
            conversation_history.append({"role": "assistant", "content": error_message})


# run the chatbot
if __name__ == "__main__":
    chat()