# Prompt Evaluation

Systematic approaches to evaluating and scoring prompt quality using evaluation pipelines and grading strategies.

## Prerequisites

- Python 3.10+
- `anthropic` and `python-dotenv` packages
- An Anthropic API key in a `.env` file (`ANTHROPIC_API_KEY=sk-...`)

## Notebooks

### 1. Prompt Eval Workflow

#### 1.1 Prompt Eval Workflow

Build an end-to-end prompt evaluation pipeline: generate test datasets using a cheaper model, run each test case through the prompt under evaluation, and collect scored results.

**Key concepts:** evaluation dataset generation, `run_prompt()`, `run_test_case()`, `run_eval()`, assistant prefill for dataset generation, `claude-haiku-4-5`

#### 1.2 Grading Strategies

Implement two grading approaches - model-based grading (LLM scores for quality, completeness, and reasoning) and code-based grading (programmatic syntax validation for JSON, Python, and regex) - then combine them into an averaged score.

**Key concepts:** model-based grading, code-based grading, `grade_by_model()`, `grade_by_syntax()`, `ast.parse()`, `json.loads()`, `re.compile()`, combined scoring
