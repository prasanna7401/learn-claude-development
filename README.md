# learn-claude-development
Built with Claude API - For developers

## 1. Claude API Basics

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

| # | Topic | Summary |
|---|-------|---------|
| 1.1 | [Prompt Eval Workflow](2_Prompt_Evaluation/1_1_Prompt_Eval_Workflow.ipynb) | Build a prompt evaluation pipeline - generate test datasets, run prompts, and score outputs |
| 1.2 | [Grading Strategies](2_Prompt_Evaluation/1_2_Grading_Strategies.ipynb) | Implement model-based and code-based grading to score prompt outputs on quality and syntax validity |

## 3. Prompt Engineering

| # | Topic | Summary |
|---|-------|---------|
| 1 | [Advanced Prompt Evaluation Workflow](3_Prompt_Engineering/1_Advanced_Prompt_Evaluation_Workflow.ipynb) | End-to-end workflow combining prompt engineering principles with automated evaluation and HTML reporting |
