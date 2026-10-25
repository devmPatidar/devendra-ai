# simple_stdio_client.py

import asyncio

from fastmcp.client import (
    Client,
    PythonStdioTransport
)


SERVER_SCRIPT = (
    "simple-server.py"
)


async def main():

    transport = PythonStdioTransport(
        script_path=SERVER_SCRIPT
    )

    async with Client(
        transport
    ) as client:

        print("\nCONNECTED\n")

        # ----------------------------------
        # DISCOVER TOOLS
        # ----------------------------------

        tools = await client.list_tools()

        print("TOOLS FOUND\n")

        for tool in tools:

            print(
                f"Name: {tool.name}"
            )

            print(
                f"Description: "
                f"{tool.description}"
            )

            print("-" * 50)

        # ----------------------------------
        # HEALTH CHECK
        # ----------------------------------

        print(
            "\nCALLING health_check\n"
        )

        result = await client.call_tool(
            "health_check",
            {}
        )

        print(result)

        # ----------------------------------
        # FLOWISE QUERY
        # ----------------------------------

        print(
            "\nCALLING ask_cis_windows11\n"
        )

        result = await client.call_tool(
            "ask_cis_windows11",
            {
                "question":
                "What is CIS Windows 11 Benchmark?"
            }
        )

        print(
            "\nRESULT\n"
        )

        print(result)


if __name__ == "__main__":

    asyncio.run(main())