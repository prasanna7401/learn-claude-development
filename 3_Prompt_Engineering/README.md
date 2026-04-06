# Prompt Engineering

Techniques for writing effective prompts - clarity, directness, and specificity - with scored before/after examples.

## Prerequisites

- Python 3.10+
- `anthropic` and `python-dotenv` packages
- An Anthropic API key in a `.env` file (`ANTHROPIC_API_KEY=sk-...`)

---

## Topics

### 1. Advanced Prompt Evaluation Workflow

End-to-end workflow combining prompt engineering principles with automated evaluation. Applies clarity, directness, and specificity techniques, then scores results using the evaluation pipeline from Section 2.

**Key concepts:** clear communication, direct instructions, specificity guidelines, prompt scoring, evaluation integration

---

## How to craft a good prompt?

### 1. Clear and Direct

Write prompts that are simple, unambiguous, and action-oriented.

| Principle | Guideline |
|-----------|-----------|
| Use simple language | Avoid jargon and roundabout phrasing |
| State the task upfront | Lead with what you want Claude to do |
| Use action verbs | Start with "Write," "Create," "Generate," "Identify", etc. |
| Give instructions, not questions | Direct commands outperform open-ended questions |

**Before:** "What should a person eat?"
> Score: 2.4

**After:** "Generate a one-day meal plan for an athlete that meets their dietary restrictions"
> Score: 6.2

### 2. Be Specific

Provide explicit guidelines or steps to direct the output.

**Guidelines** - use when you care more about the output than the process:
- Length of response
- Tone
- Important considerations
- Structure and format

**Steps** - use when the process matters:
- Troubleshooting a complex problem
- Decision making
- Critical thinking
- Following a specific process

**Example guidelines:**
```text
Guidelines:
1. Include accurate daily calorie amount
2. Show protein, fat, and carb amounts
3. Specify when to eat each meal
4. Use only foods that fit restrictions
5. List all portion sizes in grams
6. Keep budget-friendly if mentioned
```
> Score: 7.4

### 3. Structure using XML

- Makes it easy for an LLM to easily identify what and where a particular section is.
- **Use it when**: When you have a large context which includes a variety of content (doc, data, code, etc.)
- Helps you set clear boundaries for each section when working on complex prompts
> Score: 7.6

### 4. Provide Examples

- **One-shot**: Single example
- **Multi-shot**: Multiple examples
- Combine with XML tags to clearly identify input/output.
- **Explain why** something is an ideal output in an example
> Score: 7.9