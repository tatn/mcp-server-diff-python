import mcp.types as types
import pytest

from mcp_server_diff_python.server import handle_call_tool, handle_list_tools


@pytest.mark.asyncio
async def test_handle_list_tools():
    tools = await handle_list_tools()
    assert len(tools) == 1
    tool = tools[0]
    assert tool.name == "get-unified-diff"
    assert (
        tool.description
        == "Get the difference between two text articles in Unified diff format. Use this when you want to extract the difference between texts."  # noqa: E501
    )
    assert "string_a" in tool.inputSchema["properties"]
    assert "string_b" in tool.inputSchema["properties"]
    assert "string_a" in tool.inputSchema["required"]
    assert "string_b" in tool.inputSchema["required"]


@pytest.mark.asyncio
async def test_handle_call_tool():
    arguments = {
        "string_a": "line1\nline2\nline3",
        "string_b": "line1\nline2 modified\nline3",
    }
    result = await handle_call_tool("get-unified-diff", arguments)
    assert len(result) == 1
    assert isinstance(result[0], types.TextContent)
    assert result[0].type == "text"
    excepted = (
        "--- \n\n+++ \n\n@@ -1,3 +1,3 @@\n\n line1\n-line2\n+line2 modified\n line3"
    )
    assert excepted in result[0].text


@pytest.mark.asyncio
async def test_handle_call_tool_missing_arguments():
    with pytest.raises(ValueError, match="Missing arguments"):
        await handle_call_tool("get-unified-diff", None)


@pytest.mark.asyncio
async def test_handle_call_tool_unknown_tool():
    with pytest.raises(ValueError, match="Unknown tool: unknown-tool"):
        await handle_call_tool("unknown-tool", {"string_a": "a", "string_b": "b"})


@pytest.mark.asyncio
async def test_handle_call_tool_missing_string_a():
    with pytest.raises(
        ValueError, match="Missing 'string_a' or 'string_b' in arguments"
    ):
        await handle_call_tool("get-unified-diff", {"string_b": "b"})


@pytest.mark.asyncio
async def test_handle_call_tool_missing_string_b():
    with pytest.raises(
        ValueError, match="Missing 'string_a' or 'string_b' in arguments"
    ):
        await handle_call_tool("get-unified-diff", {"string_a": "a"})

        @pytest.mark.asyncio
        async def test_handle_call_tool_empty_strings():
            arguments = {"string_a": "", "string_b": ""}
            result = await handle_call_tool("get-unified-diff", arguments)
            assert len(result) == 1
            assert isinstance(result[0], types.TextContent)
            assert result[0].type == "text"
            assert result[0].text == ""

        @pytest.mark.asyncio
        async def test_handle_call_tool_identical_strings():
            arguments = {
                "string_a": "line1\nline2\nline3",
                "string_b": "line1\nline2\nline3",
            }
            result = await handle_call_tool("get-unified-diff", arguments)
            assert len(result) == 1
            assert isinstance(result[0], types.TextContent)
            assert result[0].type == "text"
            assert result[0].text == ""

        @pytest.mark.asyncio
        async def test_handle_call_tool_different_strings():
            arguments = {
                "string_a": "line1\nline2\nline3",
                "string_b": "line1\nline2\nline4",
            }
            result = await handle_call_tool("get-unified-diff", arguments)
            assert len(result) == 1
            assert isinstance(result[0], types.TextContent)
            assert result[0].type == "text"
            assert (
                "--- \n+++ \n@@ -1,3 +1,3 @@\n line1\n line2\n-line3\n+line4"
                in result[0].text
            )
