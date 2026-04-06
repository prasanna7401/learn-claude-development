# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A hands-on learning repository for the Anthropic Claude API using Python. Content is organized as numbered Jupyter notebooks, each covering a single API concept, progressing from basic to advanced.

## Repository Structure

- `1_Claude_API_Basics/` - 8 notebooks (1-7.2): requests, multi-turn conversations, chatbot exercise, system prompts, temperature, streaming, and structured output (prefill + system prompt approaches)
- `2_Prompt_Evaluation/` - 2 notebooks: prompt eval workflow and grading strategies
- `3_Prompt_Engineering/` - 1 notebook: advanced prompt evaluation workflow
- `4_Tools/` - 5 notebooks (1-5): basic flow, multi-turn conversation, streaming with fine-grained tool calls, text editor tool, web search tool
- `5_RAG/` - 5 notebooks (1-5): chunking strategies, embedding, vector DB, BM25 lexical search, multi-index RAG fusion
- `6_Special_Features/` - placeholder (currently empty, only `.env`)
- `assets/` - Diagrams and images used in documentation
- `.claude/` - Hooks (`check-notebook.py`), custom commands, settings
- `OTHERS/` - Git-ignored scratch area containing a comprehensive reference script (`0_Comprehensive_Reference.py`) and additional notebooks covering vision, extended thinking, token counting, and error handling

## Tech Stack

- **Language:** Python 3.10+
- **SDK:** `anthropic` (Anthropic Python SDK)
- **Environment:** `python-dotenv` for loading `ANTHROPIC_API_KEY` from `.env` files
- **Notebooks:** Jupyter (`.ipynb`)
- **Models used:** `claude-sonnet-4-6` (primary)

## Running Notebooks

```bash
pip install anthropic python-dotenv
# Create .env with ANTHROPIC_API_KEY=sk-ant-...
# For RAG notebooks (5_RAG/), also add VOYAGE_API_KEY=pa-...
jupyter notebook
```

Each notebook is self-contained - it installs dependencies via `%pip install` in its first cell and loads the API key from `.env` via `dotenv`. RAG notebooks require additional packages (`voyageai`, `rank-bm25`, `numpy`) installed per-notebook.

## Conventions

- **Punctuation:** Avoid em dashes; use hyphens (`-`) instead
- **Notebook naming:** `<number>_<Topic_Name>.ipynb` - number determines learning order
- **Section folders:** `<number>_<Section_Name>/` (e.g., `1_Claude_API_Basics/`)
- **Common pattern in all notebooks:** setup cell (pip install + dotenv + client init) -> markdown explanation -> code cells -> output demonstration
- **Helper functions:** `add_user_message()`, `add_assistant_message()`, `chat()` are redefined per notebook (not shared) to keep each notebook self-contained
- **`.env` files** live inside section folders (e.g., `1_Claude_API_Basics/.env`) and are git-ignored
- **`OTHERS/`** is git-ignored entirely - used for personal reference and draft content

## Key API Patterns Demonstrated

- **Structured output (Claude 3.x):** Assistant prefill with `` ```json `` + `stop_sequences` - see notebook 7.1
- **Structured output (Claude 4.x):** System prompt instruction + `re.sub()` fence stripping - see notebook 7.2 (Claude 4.x does not support assistant prefill)
- **Streaming:** Two approaches - low-level `stream=True` with event iteration, and high-level `client.messages.stream()` context manager
- **System prompt passing:** Uses `**params` dict pattern to conditionally include `system` only when not `None`
- **Tool use basic flow:** JSON schema definition + `tool_use`/`tool_result` message cycle - see `4_Tools/1_Basic_Flow.ipynb`
- **Automated tool loop:** Dispatcher loop that continues until `stop_reason != "tool_use"` - see `4_Tools/2_Multi-turn_Conversation.ipynb`
- **Streaming with fine-grained tool calls:** `stream=True` with `input_json_delta` event accumulation - see `4_Tools/3_Streaming_with_Fine-grained-Tool-Call.ipynb`
- **Built-in text editor tool:** `text_editor_20250429` tool type with view/create/str_replace/insert/undo_edit commands - see `4_Tools/4_Text_Editor_Tool.ipynb`
- **Built-in web search tool:** `web_search_20250305` tool type with `allowed_domains` filtering and citation handling - see `4_Tools/5_Web_Search_Tool.ipynb`
- **RAG pipeline:** VoyageAI embeddings + ChromaDB vector search + BM25 lexical search + Reciprocal Rank Fusion for multi-index retrieval - see `5_RAG/` notebooks

## Hooks and Commands

### PostToolUse hook

- **`check-notebook.py`** fires on `NotebookEdit` - validates that notebooks contain `%pip install`, `load_dotenv`, no hardcoded API keys, and a model variable

### Custom commands

- `/claude-api-ref` - Look up Anthropic Python SDK documentation for a given topic
- `/new-notebook-template` - Scaffold a new Jupyter notebook for this learning repository
- `/update-readmes` - Regenerate all README files from the current notebook inventory

### Formatting recommendations

- Instead of using em dashes, prefer hyphens
