# learn-claude-development

> [!NOTE]
> This repo provides a quick, high-level overview of Claude API features through code samples and related outputs - ideal for fast reference. For deeper learning, refer to the [official course](https://anthropic.skilljar.com/claude-with-the-anthropic-api) or [API documentation](https://docs.anthropic.com/en/api). Some topics covered here go beyond the course material and are based on the API documentation directly.

<details>
<summary><strong>Quick Start</strong></summary>

1. Install dependencies: `pip install anthropic python-dotenv`
2. Create a `.env` file with `ANTHROPIC_API_KEY=sk-ant-...`
3. Open any notebook: `jupyter notebook`

</details>


## 1. Claude API Basics

Core fundamentals of the Anthropic Claude API - from making your first request to getting structured output.

| # | Topic | Summary |
|---|-------|---------|
| 1 | [Making a Request](1_Claude_API_Basics/1_Making_request.ipynb) | First API call - create an Anthropic client, send a single user message, and print the response |
| 2 | [Multi-Turn Conversations](1_Claude_API_Basics/2_Multi_turn_conversations.ipynb) | Maintain conversation history by appending user/assistant messages to a list and passing it on each call |
| 3 | [ChatBot Exercise](1_Claude_API_Basics/3_ChatBot_Exercise.ipynb) | Hands-on exercise: build an interactive chatbot loop using `input()` with multi-turn conversation support |
| 4 | [System Prompts](1_Claude_API_Basics/4_System_Prompts.ipynb) | Use system prompts to define the assistant's role and boundaries (example: Math Tutor that gives hints, not answers) |
| 5 | [Temperature](1_Claude_API_Basics/5_Temperature.ipynb) | Control response creativity with the `temperature` parameter (0 = deterministic, 1 = creative) |
| 6 | [Response Streaming](1_Claude_API_Basics/6_Response_Streaming.ipynb) | Stream responses in real-time using `stream=True` and `client.messages.stream()`; explains each streaming event type |
| 7.1 | [Structured Response - Prefill](1_Claude_API_Basics/7_1_Get_Structured_Response_Prefill.ipynb) | Get structured JSON output using assistant prefill + stop sequences (Claude 3.x models) |
| 7.2 | [Structured Response - System Prompt](1_Claude_API_Basics/7_2_Get_Structured_Response_SystemPrompt.ipynb) | Get structured JSON output using a strong system prompt + regex cleanup (Claude 4.x models) |

## 2. Prompt Evaluation

Systematic approaches to evaluating and scoring prompt quality using evaluation pipelines and grading strategies.

| # | Topic | Summary |
|---|-------|---------|
| 1.1 | [Prompt Evaluation Workflow](2_Prompt_Evaluation/1_1_Prompt_Eval_Workflow.ipynb) | Build a prompt evaluation pipeline - generate test datasets, run prompts, and score outputs |
| 1.2 | [Grading Strategies](2_Prompt_Evaluation/1_2_Grading_Strategies.ipynb) | Implement model-based and code-based grading to score prompt outputs on quality and syntax validity |

## 3. Prompt Engineering

Techniques for writing effective prompts - clarity, directness, and specificity - with scored before/after examples.

| # | Topic | Summary |
|---|-------|---------|
| 1 | [Advanced Prompt Evaluation Workflow](3_Prompt_Engineering/1_Advanced_Prompt_Evaluation_Workflow.ipynb) | End-to-end workflow combining prompt engineering principles with automated evaluation and HTML reporting |

## 4. Tools

Extend Claude's capabilities by giving it access to external functions - real-time data, system integrations, and dynamic actions.

| # | Topic | Summary |
|---|-------|---------|
| 1 | [Basic Flow](4_Tools/1_Basic_Flow.ipynb) | Complete tool use lifecycle - define a function, write a JSON schema, call the API, and return tool results |
| 2 | [Multi-turn Conversation](4_Tools/2_Multi-turn_Conversation.ipynb) | Automate tool calling in a loop so Claude can make multiple tool calls across turns without manual intervention |
| 3 | [Streaming with Fine-grained Tool Calling](4_Tools/3_Streaming_with_Fine-grained-Tool-Call.ipynb) | Explore `InputJsonEvent` and buffered vs token-by-token tool argument streaming via `fine_grained=True` |
| 4 | [Text Editor Tool](4_Tools/4_Text_Editor_Tool.ipynb) | Use Claude's built-in text editor tool to view, create, and modify files via `command` dispatch; schema version varies by model |
| 5 | [Web Search Tool](4_Tools/5_Web_Search_Tool.ipynb) | Give Claude real-time web search capability using the built-in `web_search` schema; restrict results with `allowed_domains` |

## 5. RAG

Ground Claude's responses in your own documents - retrieve relevant context at query time and inject it into the prompt.

| # | Topic | Summary |
|---|-------|---------|
| 1 | [Chunking Strategies](5_RAG/1_Chunking_Strategies.ipynb) | Split documents into chunks using size-based, sentence-based, and section-based strategies with configurable overlap |
| 2 | [Embedding](5_RAG/2_Embedding.ipynb) | Convert text chunks into dense vectors using VoyageAI embeddings for semantic similarity search |
| 3 | [VectorDB](5_RAG/3_VectorDB.ipynb) | Build a full RAG pipeline with a custom VectorIndex supporting cosine similarity, top-k, threshold, and reranking retrieval |
| 4 | [BM25 Lexical Search](5_RAG/4_BM25_Lexical_Search.ipynb) | Implement BM25Index for keyword-based retrieval with TF-IDF scoring, length normalization, and term frequency saturation |
| 5 | [Multi-Index RAG](5_RAG/5_Multi-Index_RAG.ipynb) | Combine VectorIndex and BM25Index using Reciprocal Rank Fusion (RRF) to merge ranked lists from both retrieval methods |

## 6. Special Features

Unlock advanced Claude capabilities that go beyond standard text generation - extended reasoning, deeper analysis, and complex problem-solving.

| # | Topic | Summary |
|---|-------|---------|
| 1 | [Extended Thinking](6_Special_Features/1_Extended_Thinking.ipynb) | Enable Claude's internal reasoning process with `thinking` parameter for deeper analysis and multi-step logic |
| 2 | [Image and PDF Support](6_Special_Features/2_Image_and_PDF_Support.ipynb) | Send images and PDFs alongside text for vision-based analysis, description, comparison, and reasoning |
| 3 | [Citations](6_Special_Features/3_Citations.ipynb) | Enable document citations in Claude responses - `CitationPageLocation` blocks link each statement to `cited_text`, `document_index`, and page range |
| 4 | [Prompt Caching](6_Special_Features/4_Prompt_Caching.ipynb) | Mark request positions as cache breakpoints so repeated content is served from cache at a fraction of the normal input token cost |
| 5 | [Code Execution and Files API](6_Special_Features/5_Code_Execution_and_FilesAPI.ipynb) | Run code analysis with Claude's built-in code execution tool on persistant files across requests using the Files API |

## 7. MCP

Give Claude access to external tools, documents, and commands through a standardized protocol - connect any data source or capability without custom integrations.

*This section contains documentation and a CLI project example rather than notebooks. See [7_MCP/README.md](7_MCP/README.md) for details on MCP primitives (tools, resources, prompts), client/server setup, and the interactive CLI chatbot.*

---

## Resources

- [Anthropic Academy - Build with Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api)
- [Anthropic API Reference](https://docs.anthropic.com/en/api)
- [Anthropic Python SDK](https://github.com/anthropics/anthropic-sdk-python)
