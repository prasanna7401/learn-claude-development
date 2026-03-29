# Claude API Basics

Core fundamentals of the Anthropic Claude API - from making your first request to getting structured output.

## Prerequisites

- Python 3.10+
- `anthropic` and `python-dotenv` packages
- An Anthropic API key in a `.env` file (`ANTHROPIC_API_KEY=sk-...`)

---

## Notebooks

### 1. Making a Request

Send your first API call to Claude by creating an Anthropic client, building a messages list with a single user message, and printing the generated response.

**Key concepts:** `Anthropic()` client, `messages.create()`, `model`, `max_tokens`, `message.content[0].text`

---

### 2. Multi-Turn Conversations

Maintain conversation context by appending user and assistant messages to a list and passing the full history on each API call. Demonstrates how LLMs are stateless and require explicit conversation tracking.

**Key concepts:** conversation history, `role: user`, `role: assistant`, helper functions (`add_user_message`, `add_assistant_message`, `chat`)

---

### 3. ChatBot Exercise

Hands-on exercise to build an interactive chatbot using Python's `input()` function in a loop, combining multi-turn conversation tracking with real user input.

**Key concepts:** `input()` loop, `KeyboardInterrupt` handling, interactive multi-turn chat

---

### 4. System Prompts

Define the assistant's role, behavior, and response boundaries using system prompts. Builds a Math Tutor specialist that gives hints instead of answers and rejects off-topic questions.

**Key concepts:** `system` parameter, `**params` dict pattern, role-based prompting, behavioral constraints

---

### 5. Temperature

Control how predictable or creative responses are using the `temperature` parameter (0.0-1.0). Covers tokenization, prediction, and sampling concepts.

**Key concepts:** `temperature`, low/medium/high temperature use cases, tokenization, prediction, sampling

---

### 6. Response Streaming

Stream responses in real-time instead of waiting for the full response. Covers two approaches: low-level `stream=True` with raw event iteration, and high-level `client.messages.stream()` context manager.

**Key concepts:** `stream=True`, `client.messages.stream()`, `text_stream`, `get_final_message()`, streaming event types (`RawMessageStartEvent`, `RawContentBlockDeltaEvent`, etc.)

---

### 7. Structured Output

#### 7.1 Prefill Method

Get clean JSON output by pre-populating the assistant turn with a JSON code fence and using `stop_sequences` to halt at the closing fence. Works with models that support assistant prefill.

**Key concepts:** assistant prefill, `stop_sequences`, `json.loads()`, `claude-haiku-4-5`

#### 7.2 System Prompt Method

Get clean JSON output from Claude 4.x models (which do not support assistant prefill) by using a strong system prompt instruction combined with regex fence stripping as a safety net.

**Key concepts:** system prompt JSON instruction, `re.sub()` fence stripping, `claude-sonnet-4-6`
