# Special Features

Unlock advanced Claude capabilities that go beyond standard text generation - extended reasoning, deeper analysis, and complex problem-solving.

## Prerequisites

- Python 3.10+
- `anthropic` and `python-dotenv` packages
- An Anthropic API key in a `.env` file (`ANTHROPIC_API_KEY=sk-...`)

---

## Topics

### 1. Extended Thinking

Enable Claude's internal reasoning process for tasks that require deeper analysis, multi-step logic, or careful deliberation. Claude produces a thinking block before its final response, giving you visibility into how it approached the problem.

#### The `thinking` Parameter

Pass a `thinking` dict to `messages.create()` to enable extended thinking:

```python
params["thinking"] = {
    "type": "enabled",
    "budget_tokens": 1024,  # minimum value
}
```

> [!IMPORTANT]
> - `budget_tokens` must be **at least 1024**
> - `max_tokens` must always be **greater than** `budget_tokens`
> - The actual token budget for text generation is `max_tokens - budget_tokens`

#### `ThinkingBlock` vs `RedactedThinkingBlock`

When thinking is enabled, Claude's response `content` list will contain one or more thinking blocks alongside the usual `TextBlock`.

<table>
<tr>
<th width="50%">ThinkingBlock</th>
<th width="50%">RedactedThinkingBlock</th>
</tr>
<tr>
<td valign="top">

The standard thinking block. Contains Claude's visible reasoning and a cryptographic `signature` that verifies the block was produced by the model.

```python
ThinkingBlock(
    type='thinking',
    thinking="I'll approach this by...",
    signature='EtkCCmQ...'  # do NOT modify
)
```

</td>
<td valign="top">

Returned when Claude's internal safety systems flag the thinking content. The thinking is encrypted and not human-readable, but must still be passed back in follow-up requests.

```python
RedactedThinkingBlock(
    type='redacted_thinking',
    data='<encrypted>'  # pass back as-is
)
```

</td>
</tr>
</table>

> [!WARNING]
> Never modify thinking blocks - especially the `signature` field. The API uses the signature to verify block integrity. Pass all thinking blocks back unchanged in multi-turn conversations.

#### Handling Both Block Types

Your client application must handle both block types:

```python
from anthropic.types import ThinkingBlock, RedactedThinkingBlock

for block in response.content:
    if isinstance(block, ThinkingBlock):
        print(f"Thinking: {block.thinking}")
    elif isinstance(block, RedactedThinkingBlock):
        # Pass back as-is - do not inspect or modify
        pass
    else:
        print(f"Response: {block.text}")
```

#### Testing `RedactedThinkingBlock`

You can force a `RedactedThinkingBlock` response during development using a special trigger string as your message content. This lets you verify your application handles the redacted case correctly before encountering it in production.

> This magic string trigger may not work on the latest model versions.


**Key concepts:** `thinking` parameter, `budget_tokens`, `ThinkingBlock`, `RedactedThinkingBlock`, `signature`, thinking constraints

---

### 2. Image and PDF Support

Send images alongside text to leverage Claude's vision capabilities for analysis, description, comparison, and reasoning.

#### Limits

- Up to **100 images** total across all messages in a single request
- Max **5MB** per image

#### Resolution Limits (model-dependent)

| Scenario | Max dimension |
|---|---|
| Single image | 8000px (height or width) |
| Multiple images | 2000px (height or width) |

#### Input Formats

- `base64` - encoded image bytes sent directly in the request
- `url` - a URL pointing to a publicly accessible image

#### Encoding Pattern

Read image bytes and encode to a base64 string:

```python
import base64
with open("./assets/image.png", "rb") as f:
    image_bytes = base64.standard_b64encode(f.read()).decode("utf-8")
```

Pass it in the message content as an `ImageBlock` source:

```json
{
    "type": "image",
    "source": {
        "type": "base64",
        "media_type": "image/png",
        "data": image_bytes,
    }
}
```
> [!TIP]
> Use specific instructions, guidelines, steps, or examples to get better results from image-based requests. Tell LLM exactly what to look for or describe.

#### Token Estimation

Image tokens are proportional to pixel area:

$$\text{tokens} = \frac{\text{width (px)} \times \text{height (px)}}{750}$$

> For example, a 1500x1000px image costs approximately 2000 tokens.

**Key concepts:** `ImageBlock`, `base64` encoding, URL source, image limits, token estimation

#### PDF Support

Similar to image handling, but uses `document` type instead of `image`.

#### Input Format

```json
{
    "type": "document",
    "source": {
        "type": "base64",
        "media_type": "application/pdf",
        "data": file_bytes
    }
}
```

**Key concepts:** `DocumentBlock`, `base64` encoding, `application/pdf` media type

---

### 3. Citations

Enable Claude to cite the exact source text from PDF documents it references. When citations are enabled, each response `TextBlock` includes a `citations` list of `CitationPageLocation` objects that link Claude's statements back to the original document.

#### Citation Structure

Each `CitationPageLocation` object contains:

| Field | Type | Description |
|-------|------|-------------|
| `cited_text` | `str` | Verbatim excerpt from the source document that supports the statement |
| `document_index` | `int` | Zero-based index of the source document (e.g., `0` for the first document) |
| `document_title` | `str` | Filename of the source document (e.g., `"earth.pdf"`) |
| `start_page_number` | `int` | First page the cited text appears on |
| `end_page_number` | `int` | Last page the cited text appears on |

> [!TIP]
> Use the `citations` list from each `TextBlock` in client applications to render interactive, clickable citations that jump directly to the referenced page in the source document.

**Key concepts:** `"citations": {"enabled": True}`, `CitationPageLocation`, `cited_text`, `document_index`, `document_title`, `start_page_number`, `end_page_number`

---

### 4. Prompt Caching

Prompt caching lets you mark specific positions in a request as **cache breakpoints**. When a subsequent request matches all content up to a breakpoint exactly, the API returns a cache hit and charges a fraction of the normal input token price - instead of reprocessing those tokens from scratch.

> [!TIP]
> Place breakpoints on content that changes least frequently - system prompts, tool definitions, and large reference documents. Leave the frequently-changing parts (user questions, recent conversation turns) without breakpoints.

#### `cache_control` Parameter

Add `"cache_control": {"type": "ephemeral"}` to the last content block of any section you want to cache. The cache persists for approximately 5 minutes (refreshed on each hit), and 1-hour extended TTL at higher cost.

```python
# Mark the end of a long system prompt as a cache breakpoint
system = [
    {
        "type": "text",
        "text": "You are a helpful assistant with extensive knowledge...",
        "cache_control": {"type": "ephemeral"}   # breakpoint here
    }
]
```

> [!IMPORTANT]
> - A cached block must contain at least **1024 tokens** (Claude Haiku) or **2048 tokens** (Claude Sonnet/Opus). Shorter blocks are silently ignored and will never produce a cache hit.
> - You may place at most **4 cache breakpoints** per request. Additional breakpoints beyond 4 are ignored.

Usage counters in the response tell you what happened:

| Counter | Meaning |
|---|---|
| `cache_creation_input_tokens` | Tokens written to cache this request (charged at ~1.25x) |
| `cache_read_input_tokens` | Tokens read from cache (charged at ~0.1x) |
| `input_tokens` | Non-cached tokens processed normally (charged at 1x) |

#### Cache Ordering

The API evaluates cache breakpoints **left to right** in a fixed order regardless of how you structure your request:

```
system prompt  →  tools / tool_results  →  messages (oldest → newest)
```

A cache hit at breakpoint N requires every token **from the start of the request up to and including breakpoint N** to be byte-identical to a prior cached request. If any content before breakpoint N differs, that breakpoint and all subsequent ones miss.

> [!TIP]
> Structure your requests so the most expensive-to-process content (large documents, long system prompts) sits before the earliest breakpoint, and the content most likely to vary (the user's current question) sits after the last one. This maximizes hit rate and minimizes cost.

**Key concepts:** `cache_control`, cache breakpoints, `cache_creation_input_tokens`, `cache_read_input_tokens`, `input_tokens`, TTL, cache ordering

---

### 5. Code Execution and Files API

**Files API**: Upload files ahead of time and reference them via `file_id` in subsequent API calls
> [!WARNING]
> - Files are scoped to the API key's workspace - also accessible by other keys in the same workspace! 
> - Be considerate of the file upload limits.

**Code Execution Tool**: Runs code in a containerized environment to perform complex/advanced actions and returns the results to Claude.
> This runs in an isolated Docker container with NO network access

**Files API + Code Execution Tool (combined pattern)**

1. Upload a file to get a `file_id`
2. Add a `ContainerUploadBlock` to the user message:
   ```python
   {"type": "container_upload", "file_id": file_metadata.id}
   ```
3. Claude executes code on the file inside the container
4. Output is returned in a `code_execution_tool_result` block; any files created by the code appear as `code_execution_output` type content

**Key concepts:** Files API, `file_id`, `ContainerUploadBlock`, `code_execution_tool_result`, `code_execution_output`, containerized execution