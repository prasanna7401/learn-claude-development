# learn-claude-development
Built with Claude API - For developers

## 1. Claude API Basics

| # | Notebook | Summary |
|---|----------|---------|
| 1 | `1_Making_request.ipynb` | First API call — create an Anthropic client, send a single user message, and print the response |
| 2 | `2_Multi_turn_conversations.ipynb` | Maintain conversation history by appending user/assistant messages to a list and passing it on each call |
| 3 | `3_ChatBot_Exercise.ipynb` | Hands-on exercise: build an interactive chatbot loop using `input()` with multi-turn conversation support |
| 4 | `4_System_Prompts.ipynb` | Use system prompts to define the assistant's role and boundaries (example: Math Tutor that gives hints, not answers) |
| 5 | `5_Temperature.ipynb` | Control response creativity with the `temperature` parameter (0 = deterministic, 1 = creative) |
| 6 | `6_Response_Streaming.ipynb` | Stream responses in real-time using `stream=True` and `client.messages.stream()`; explains each streaming event type |
| 7.1 | `7_1_Get_Structured_Response_Prefill.ipynb` | Get structured JSON output using assistant prefill + stop sequences (Claude 3.x models) |
| 7.2 | `7_2_Get_Structured_Response_SystemPrompt.ipynb` | Get structured JSON output using a strong system prompt + regex cleanup (Claude 4.x models) |

## 2. Prompt Evaluation

| # | Notebook | Summary |
|---|----------|---------|
| 1 | `1_Prompt_Eval_Workflow.ipynb` | Set up a prompt evaluation workflow to systematically test and compare prompt variations |
