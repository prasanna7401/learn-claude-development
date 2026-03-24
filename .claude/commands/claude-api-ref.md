Look up Anthropic Python SDK documentation for the given topic.

The user will provide a topic keyword such as: $ARGUMENTS

Use the `claude-api` skill to retrieve relevant API patterns, code examples, and usage guidance from the Anthropic Python SDK.

Common topics include:
- **messages** — `client.messages.create()` basics, parameters, response structure
- **streaming** — `stream=True` event iteration vs `client.messages.stream()` context manager
- **tool use** — tool definitions, tool_choice, handling tool_use/tool_result blocks
- **vision** — image content blocks (base64, URL), multi-modal messages
- **extended thinking** — thinking blocks, budget_tokens, streaming thinking
- **system prompts** — system parameter, multi-block system prompts
- **structured output** — JSON mode, assistant prefill (Claude 3.x), system prompt instruction (Claude 4.x)
- **token counting** — `client.messages.count_tokens()`, usage in responses
- **error handling** — APIError, RateLimitError, retry strategies
- **batches** — `client.messages.batches`, async batch processing
- **prompt caching** — cache_control blocks, ephemeral caching

After retrieving the information, format it as a concise reference with:
1. A brief explanation of the concept
2. A minimal working code example using the `anthropic` Python SDK
3. Key parameters and their purpose
4. Common pitfalls or tips relevant to this notebook-based learning repo
