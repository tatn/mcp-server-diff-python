# mcp-server-diff-python MCP server

テキストの差分を取得するためのMCPサーバーです。
Pythonの標準ライブラリ`difflib`を利用して、2つのテキスト間の差分をUnified diff形式で提供します。

## 機能

### ツール

サーバーは以下の単一のツールを提供します：

- **get-unified-diff**: 2つのテキスト間の差分をUnified diff形式で取得します
  - 引数：
    - `string_a`: 比較元のテキスト（必須）
    - `string_b`: 比較先のテキスト（必須）
  - 戻り値：Unified diff形式のテキスト

## インストール方法

### Claude Desktop

#### MacOS
設定ファイルのパス: `~/Library/Application\ Support/Claude/claude_desktop_config.json`

#### Windows
設定ファイルのパス: `%APPDATA%/Claude/claude_desktop_config.json`

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

## 開発
### デバッグ



[`npm`](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)を使用して、以下のコマンドでMCP Inspectorを起動できます：

```bash
npx @modelcontextprotocol/inspector uv --directory path\to\mcp-server-diff-python run mcp-server-diff-python
```

```bash
npx @modelcontextprotocol/inspector uvx mcp-server-diff-python
```

