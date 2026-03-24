# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A hands-on learning repository for the Anthropic Claude API using Python. Content is organized as numbered Jupyter notebooks, each covering a single API concept, progressing from basic to advanced.

## Repository Structure

- `1_Claude_API_Basics/` - Numbered notebooks (1-7) covering core API features: requests, multi-turn conversations, system prompts, temperature, streaming, and structured output
- `OTHERS/` - Git-ignored scratch area containing a comprehensive reference script (`0_Comprehensive_Reference.py`) and additional notebooks (8-12) covering tool use, vision, extended thinking, token counting, and error handling

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
jupyter notebook
```

Each notebook is self-contained - it installs dependencies via `%pip install` in its first cell and loads the API key from `.env` via `dotenv`.

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


### Formatting recommendations

- Instead of using em dashes, prefer hypens