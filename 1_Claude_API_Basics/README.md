# Claude API Basics

Getting started with the Anthropic Python SDK - from your first API call to structured JSON output.

## Prerequisites

- Python 3.10+
- `anthropic` and `python-dotenv` packages
- An Anthropic API key in a `.env` file (`ANTHROPIC_API_KEY=sk-...`)

## Notebooks

### 1. Making a Request

Create an `Anthropic` client, send a single user message via `client.messages.create()`, and print the response. Covers the minimal setup needed to talk to Claude.

**Key concepts:** `Anthropic()` client, `messages.create()`, `model`, `max_tokens`, reading `message.content[0].text`

---

### 2. Multi-Turn Conversations

LLMs are stateless - they don't remember previous turns. This notebook shows how to maintain conversation history by appending user/assistant messages to a list and passing the full list on each call.

**Key concepts:** message list pattern, helper functions (`add_user_message`, `add_assistant_message`, `chat`), conversation context

---

### 3. ChatBot Exercise

Hands-on exercise: build an interactive chatbot loop using Python's `input()` with multi-turn conversation support. Combines the patterns from notebooks 1 and 2 into a working CLI chat.

**Key concepts:** `while True` loop, `input()`, `KeyboardInterrupt` handling, full conversation flow

---

### 4. System Prompts

Use the `system` parameter to define the assistant's role and boundaries. The example builds a **Math Tutor** that gives hints instead of direct answers and refuses off-topic questions.

**Key concepts:** `system` parameter, role definition, behavioral DOs/DON'Ts, passing `system` via `**params` to handle `None` gracefully

---

### 5. Temperature

Control response creativity with the `temperature` parameter (0 = deterministic, 1 = creative).

| Low (0.0-0.3) | Medium (0.4-0.7) | High (0.8-1.0) |
|---|---|---|
| Facts, coding, data extraction | Summaries, education, problem-solving | Brainstorming, creative writing, marketing |

**Key concepts:** `temperature` parameter, tokenization, prediction, sampling

---

### 6. Response Streaming

Stream responses in real-time instead of waiting for the full completion. Covers two approaches:
- **Low-level:** `stream=True` with manual event iteration
- **High-level:** `client.messages.stream()` context manager with `.text_stream`

**Key concepts:** `stream=True`, `client.messages.stream()`, event types (`MessageStart`, `ContentBlockDelta`, `MessageStop`), `stream.get_final_message()`

---

### 7 Structured Response

#### 7.1 Structured Response - Prefill Method

Get clean JSON output by pre-filling the assistant turn with `` ```json `` and using `stop_sequences=["```"]` to cut off the closing fence. Works with **Claude 3.x models** (e.g. `claude-3-haiku-20240307`).

**Key concepts:** assistant prefill, `stop_sequences`, `json.loads()` on raw output


#### 7.2 Structured Response - System Prompt Method

Get clean JSON output using a strong system prompt that instructs the model to return raw JSON only, plus a `re.sub()` safety net to strip any markdown fences. Works with **Claude 4.x models** (e.g. `claude-sonnet-4-6`) which don't support assistant prefill.

**Key concepts:** system prompt for format control, regex cleanup, `json.loads()` validation
