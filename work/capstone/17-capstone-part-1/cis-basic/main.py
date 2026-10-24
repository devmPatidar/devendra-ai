from assistants.policy_agent_enhanced import build_assistant
from utils.formatter import display_response

def main():
    assistant = build_assistant()

    print("\n🚀 CIS Policy Intelligence Agent\n")

    while True:
        query = input("Ask CIS Policy > ")

        if query.lower() in ["exit", "quit"]:
            break

        result = assistant(query)

        display_response(result)

# ------------------------------------------------------------------------
# Use for enhanced agent with memory and query classification
# ------------------------------------------------------------------------

"""
from agents.policy_agent import build_agent
from utils.formatter import display_response
from utils.saver import save_response

def main():
    agent = build_agent()

    print("\n🚀 CIS Policy Intelligence Agent (Enhanced)\n")

    while True:
        query = input("Ask CIS Policy > ")

        if query.lower() in ["exit", "quit"]:
            break

        result = agent(query)

        display_response(result)

        save_response(result["query"], result["answer"])

if __name__ == "__main__":
    main()

"""

if __name__ == "__main__":
    main()