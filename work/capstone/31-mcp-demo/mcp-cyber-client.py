import asyncio
from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_mcp_adapters.client import MultiServerMCPClient

load_dotenv()

with open(r"C:\Users\user\Desktop\devendra-ai\work\key-vault\openai\open-ai-api.key") as f:
    openai_api_key = f.read().strip()

async def main():

    client = MultiServerMCPClient(
        {
            "cyber": {
                "transport": "stdio",
                "command": "python",
                "args": ["mcp_cyber_tools_server.py"],
            }
        }
    )

    tools = await client.get_tools()

    print("\nAvailable Tools\n----------------")
    for t in tools:
        print(t.name)

    llm = ChatOpenAI(
        model="gpt-4.1",
        api_key=openai_api_key,
        temperature=0,
    )

    agent = create_agent(
        model=llm,
        tools=tools,
    )

    response = await agent.ainvoke(
        {
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "Use only the tools supplied to you. Do not invent or call "
                        "any tool that is not in the supplied tool list."
                    ),
                },
                {
                    "role": "user",
                    "content": (
                        "Recommend CIS controls for Apache HTTP Server and Include recent CVEs."
                    ),
                }
            ]
        }
    )

    print("\nTools Used\n----------------")
    tools_used = {
        tool_call["name"]
        for message in response["messages"]
        for tool_call in getattr(message, "tool_calls", [])
    }
    if tools_used:
        for tool_name in tools_used:
            print(tool_name)
    else:
        print("No tools used")

    print("\n===========================")
    print(response["messages"][-1].content)

if __name__ == "__main__":
    asyncio.run(main())