"""
==================================================
SIMPLE FLOWISE MCP SERVER
==================================================

Purpose:
    1. Wrap Flowise endpoint as MCP Tool
    2. Expose tool via MCP Server
    3. Demonstrate MCP integration

Requirements:

    pip install fastmcp
    pip install requests

Run:

    python simple_flowise_mcp_server.py

==================================================
"""

import requests

from fastmcp import FastMCP


# ==================================================
# CONFIGURATION
# ==================================================

FLOWISE_API_URL = (
    "https://cloud.flowiseai.com/"
    "api/v1/prediction/"
    "034ff02d-e9e0-4003-937d-6c37ea84e157"
)


# ==================================================
# MCP SERVER
# ==================================================

mcp = FastMCP(
    name="simple-flowise-server"
)


# ==================================================
# TOOL 1
# ==================================================

@mcp.tool
def health_check():

    """
    Simple health check.
    """

    return {
        "status": "healthy"
    }


# ==================================================
# TOOL 2
# ==================================================

@mcp.tool
def ask_cis_windows11(question: str) -> str:
    """Query the Flowise workflow knowledge base for CIS benchmarks and security guidance.

    Args:
        question: The security question or topic to search.
    """
    url = "http://localhost:7860/api/v2/workflows"
    headers = {
        "Content-Type": "application/json",
        "x-api-key": "sk-qNz-70oQVfAE8wvyRadRAVpwVDbfBtxcj_ivZNHx_Ow",
    }
    payload = {
        "flow_id": "eef87fb7-0ffe-4987-9be8-2e17813b7eb0",
        "input_value": question,
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=30)
        response.raise_for_status()
        result = response.json()

        # Safely extract output text
        return result.get("output", {}).get("text", "No output returned.")
    except requests.RequestException as e:
        return f"Error executing CIS workflow request: {e}"


# ==================================================
# MAIN
# ==================================================

if __name__ == "__main__":

    print(
        "\nStarting MCP Server..."
    )

    print(
        "\nRegistered Tools:"
    )

    print(
        "- health_check"
    )

    print(
        "- ask_cis_windows11"
    )

    mcp.run()