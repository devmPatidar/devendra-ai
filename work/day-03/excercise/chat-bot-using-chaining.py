from pathlib import Path
from uuid import uuid4

from langchain_core.messages import BaseMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI


OPENAI_API_KEY_PATH = Path(
    r"C:\Users\user\Desktop\devendra-ai\work\key-vault\openai\open-ai-api.key"
)
MODEL_NAME = "gpt-4o-mini"


def load_api_key():
    try:
        api_key = OPENAI_API_KEY_PATH.read_text(encoding="utf-8").strip()
    except OSError as error:
        raise OSError(f"Unable to read the OpenAI API key file: {OPENAI_API_KEY_PATH}") from error

    if not api_key:
        raise ValueError(f"The OpenAI API key file is empty: {OPENAI_API_KEY_PATH}")

    return api_key


def create_conversation_chain(model):
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant. Use the conversation history when relevant."),
            MessagesPlaceholder(variable_name="messages"),
        ]
    )
    return prompt | model


def new_session_id(session_ids: set[str]) -> str:
    session_id = f"session-{uuid4().hex[:8]}"
    while session_id in session_ids:
        session_id = f"session-{uuid4().hex[:8]}"
    return session_id


def chat():
    try:
        model = ChatOpenAI(
            api_key=load_api_key(),
            model=MODEL_NAME,
            temperature=0.7,
            max_tokens=512,
        )
    except Exception as error:
        print(f"Unable to initialize the OpenAI chatbot: {error}")
        return

    conversation = create_conversation_chain(model)
    session_ids = set()
    session_histories: dict[str, list[BaseMessage]] = {}
    active_session_id = new_session_id(session_ids)
    session_ids.add(active_session_id)
    session_histories[active_session_id] = []
    print("Welcome to the OpenAI chatbot! Type 'exit', 'quit', or 'end' to stop.")
    print(f"Session: {active_session_id}")
    print("Commands: /new, /sessions, /switch <session-id>")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in {"exit", "quit", "end"}:
            print("Goodbye!")
            break
        if user_input == "/new":
            active_session_id = new_session_id(session_ids)
            session_ids.add(active_session_id)
            session_histories[active_session_id] = []
            print(f"Started new session: {active_session_id}")
            continue
        if user_input == "/sessions":
            for session_id in sorted(session_ids):
                marker = " (active)" if session_id == active_session_id else ""
                print(f"{session_id}{marker}")
            continue
        if user_input == "/switch" or user_input.startswith("/switch "):
            command_parts = user_input.split(maxsplit=1)
            if len(command_parts) == 1:
                print("Usage: /switch <session-id>")
            elif command_parts[1] not in session_ids:
                print("Unknown session ID. Use /sessions to list available sessions.")
            else:
                active_session_id = command_parts[1]
                print(f"Switched to session: {active_session_id}")
            continue
        if user_input.startswith("/"):
            print("Commands: /new, /sessions, /switch <session-id>, exit")
            continue
        if not user_input:
            continue

        try:
            user_message = HumanMessage(content=user_input)
            response = conversation.invoke(
                {"messages": [*session_histories[active_session_id], user_message]}
            )
            session_histories[active_session_id].extend([user_message, response])
            print(f"Bot: {response.content}")
        except Exception as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    chat()