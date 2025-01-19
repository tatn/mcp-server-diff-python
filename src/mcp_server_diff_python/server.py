import difflib

import mcp.server.stdio
import mcp.types as types
from mcp.server import NotificationOptions, Server
from mcp.server.models import InitializationOptions

server = Server("mcp-server-diff-python")


@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    """
    List available tools.
    Each tool specifies its arguments using JSON Schema validation.
    """
    return [
        types.Tool(
            name="get-unified-diff",
            description="Get the difference between two text articles in Unified diff format. Use this when you want to extract the difference between texts.",  # noqa: E501
            inputSchema={
                "type": "object",
                "properties": {
                    "string_a": {"type": "string"},
                    "string_b": {"type": "string"},
                },
                "required": ["string_a", "string_b"],
            },
        )
    ]


@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict | None
) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """
    Handle tool execution requests.
    Tools can modify server state and notify clients of changes.
    """
    if name != "get-unified-diff":
        raise ValueError(f"Unknown tool: {name}")

    if not arguments:
        raise ValueError("Missing arguments")

    string_a: str = arguments.get("string_a")
    string_b: str = arguments.get("string_b")

    if string_a is None or string_b is None:
        raise ValueError("Missing 'string_a' or 'string_b' in arguments")

    diff_iterator = difflib.unified_diff(string_a.splitlines(), string_b.splitlines())

    return [types.TextContent(type="text", text="\n".join(diff_iterator))]


async def main():
    # Run the server using stdin/stdout streams
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="mcp-server-diff-python",
                server_version="0.1.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )
