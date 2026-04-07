# MCP (Model Context Protocol)

Give Claude access to external tools, documents, and commands through a standardized protocol - connect any data source or capability without custom integrations.

## Prerequisites

- Python 3.10+
- `mcp[cli]` package (MCP SDK)
- Anthropic API key in a `.env` file (`ANTHROPIC_API_KEY=sk-...`)

---

## What is MCP?

MCP (Model Context Protocol) is a standardized protocol for connecting LLMs to external tools, data sources, and capabilities. Instead of building custom integrations for each tool, MCP provides a universal interface.

### Three Primitives

| Primitive | Controlled By | Purpose |
|---|---|---|
| **Tools** | Assistant (LLM) | Functions the model can call autonomously (e.g., read a file, query a database) |
| **Resources** | Client application | Data endpoints the app exposes to the model (e.g., `docs://documents`) |
| **Prompts** | User | Pre-built prompt templates invoked by the user (e.g., `/summarize`) |

### Tool Creation

Tools are functions the assistant can call autonomously. Define them with type annotations and descriptions so the model knows when and how to use them:

```python
from mcp.server.fastmcp import FastMCP
from pydantic import Field
from typing import Annotated

mcp = FastMCP("DocumentMCP", log_level="ERROR")

@mcp.tool(
    name="add_int",
    description="Add two integers together",
)
def add_integer(
    a: Annotated[int, Field(description="First integer")],
    b: Annotated[int, Field(description="Second integer")],
) -> int:
    return a + b

if __name__ == "__main__":
    mcp.run(transport="stdio")
```

### Resources (@ References)

Resources are data endpoints that the client application controls. The client sends a `ReadResourceRequest` to the MCP server, which returns a `ReadResourceResult` with the requested data.

Two resource types based on URI pattern:

- **Direct** - no parameters, returns a fixed resource (e.g., `docs://documents`)
- **Templated** - one or more parameters in the URI (e.g., `docs://documents/{doc_id}`)

```python
@mcp.resource(
    "docs://documents",
    mime_type="application/json",  # hint to client: can be text, json, or binary
)
def list_documents() -> str:
    # return list of available documents
    ...
```

### Prompts (/ Commands)

Prompts are user-controlled templates - pre-built instructions the user can invoke explicitly:

```python
@mcp.prompt(
    name="summarize_doc",
    description="Summarize the contents of a document. Input is the filename.",
)
def summarize_doc(
    doc_id: Annotated[str, Field(description="The ID of the document to summarize")],
) -> list[base.Message]:
    ...
```

**Key concepts:** FastMCP, tools, resources, prompts, type annotations, Pydantic Field descriptions, STDIO transport

---

## MCP Server Inspector

For troubleshooting and testing your MCP server during development, use the built-in inspector:

```sh
mcp dev mcp_server.py
```

This launches an interactive UI where you can list tools, call them with test inputs, browse resources, and invoke prompts - all without writing a client.

---

## MCP Client Setup

The MCP client manages the connection to one or more MCP servers. Key components:

- **`MCPClient` class** - wraps the connection lifecycle with a cleanup function for proper resource management
- **Client Session** - the actual connection to the server, wrapped inside the `MCPClient` class

The client exposes methods to:
- `list_tools()` / `call_tool()` - discover and invoke tools
- `list_prompts()` / `get_prompt()` - discover and retrieve prompt templates
- `read_resource()` - fetch resource data by URI

**Key concepts:** MCPClient, Client Session, async context manager, tool discovery, resource reading

---

## CLI Project

The `cli_project/` directory contains a complete working example - an interactive CLI chatbot that connects Claude to a document repository via MCP.

### Features

- **Chat** - natural conversation with Claude
- **`@doc_id`** - mention a document to inject its content as context
- **`/command`** - invoke MCP prompts like `/summarize_doc`
- **Tool execution** - Claude autonomously reads and edits documents via MCP tools
- **Auto-completion** - interactive suggestions for both `@` references and `/` commands

See [`cli_project/README.md`](cli_project/README.md) for setup and usage instructions.

---

## Adding MCP Server to Claude Code

Register any MCP server with Claude Code using:

```sh
claude mcp add [server-name] [command-to-start-server]
```

Once added, Claude Code can discover and use the server's tools, resources, and prompts during conversations.

---

## Advanced MCP Topics

For advanced topics like **Sampling**, **Notifications**, **Roots**, **Transport methods**

For a detailed implementation example, see [learn-mcp/mcp_advanced_anthropic](https://github.com/prasanna7401/learn-mcp/tree/main/mcp_advanced_anthropic/).
