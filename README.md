# mcp-server-diff-python

An MCP server for obtaining text differences between two strings.
This server leverages Python's standard library `difflib` to efficiently generate and provide differences between two texts in Unified diff format, making it ideal for text comparison and version control purposes.

<a href="https://glama.ai/mcp/servers/qbwsx2g4vd"><img width="380" height="200" src="https://glama.ai/mcp/servers/qbwsx2g4vd/badge" alt="Server Diff Python MCP server" /></a>

## Features

### Tools

The server provides a single tool:

- **get-unified-diff**: Get differences between two texts in Unified diff format
  - Arguments:
    - `string_a`: Source text for comparison (required)
    - `string_b`: Target text to compare against (required)
  - Return value: A string containing the differences in Unified diff format

## Usage

### Claude Desktop

Using with Claude Desktop
To use with Claude Desktop, add the server config:

On MacOS:  `~/Library/Application\ Support/Claude/claude_desktop_config.json`  
On Windows: `%APPDATA%/Claude/claude_desktop_config.json`

```json
"mcpServers": {
  "mcp-server-diff-python": {
    "command": "uvx",
    "args": [
      "mcp-server-diff-python"
    ]
  }
}
```

or Add the following configuration:

```bash
git clone https://github.com/tatn/mcp-server-diff-python.git
cd mcp-server-diff-python
uv sync
uv build
```

```json
"mcpServers": {
  "mcp-server-diff-python": {
    "command": "uv",
    "args": [
      "--directory",
      "path\\to\\mcp-server-diff-python",
      "run",
      "mcp-server-diff-python"
    ]
  }
}
```

## Development
### Debugging

You can start the MCP Inspector using [npx](https://docs.npmjs.com/cli/v11/commands/npx)with the following commands:

```bash
npx @modelcontextprotocol/inspector uvx mcp-server-diff-python
```

```bash
npx @modelcontextprotocol/inspector uv --directory path\to\mcp-server-diff-python run mcp-server-diff-python
```

