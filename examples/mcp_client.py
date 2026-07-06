"""Example: MCP Client Usage.

This example demonstrates how to use the MCP Server
with AI agents like Claude Desktop.
"""

import json
from typing import Any

from socialmedia_hub.mcp.server import create_mcp_server


def main():
    """Main function."""
    # Create MCP server
    mcp = create_mcp_server(
        api_key="YOUR_API_KEY",
        base_url="http://127.0.0.1:8000"
    )

    # List all available tools
    print("=== Available MCP Tools ===")
    tools = mcp.list_tools()
    print(f"Total tools: {len(tools)}")

    # Group tools by platform
    platforms = {}
    for tool in tools:
        platform = tool["name"].split("_")[0]
        if platform not in platforms:
            platforms[platform] = []
        platforms[platform].append(tool["name"])

    print("\nTools by platform:")
    for platform, tool_names in sorted(platforms.items()):
        print(f"  {platform}: {len(tool_names)} tools")

    # Example: Call a tool
    print("\n=== Example Tool Call ===")
    result = mcp.call_tool(
        "health_check",
        {}
    )
    print(f"Health check result: {json.dumps(result, indent=2)}")

    # Export MCP configuration for Claude Desktop
    print("\n=== Claude Desktop Configuration ===")
    config = {
        "mcpServers": {
            "socialmedia-hub": {
                "command": "npx",
                "args": [
                    "mcp-remote",
                    "http://127.0.0.1:8000/api/v1/mcp/sse",
                    "--header",
                    "Authorization: Bearer YOUR_API_KEY"
                ]
            }
        }
    }
    print(json.dumps(config, indent=2))


if __name__ == "__main__":
    main()
