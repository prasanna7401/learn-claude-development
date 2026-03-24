Scaffold a new Jupyter notebook for this learning repository.

**Topic name** is provided via `$ARGUMENTS`. If empty, ask the user for the topic name in Title_Case with underscores (e.g. `Token_Counting`).

**Auto-detect notebook number:** Scan `*.ipynb` files in the current working directory, extract numeric prefixes (the leading digits before the first `_`), and use `max + 1`. If no `.ipynb` files exist, start at `1`.

**Section folder:** Use the current working directory (do not ask).

Then:

1. Create a `.ipynb` file at `<number>_<Topic_Name>.ipynb` with this structure:

**Cell 1 — Markdown (topic header):**
```markdown
# <Topic Name (spaces instead of underscores)>

<Brief description placeholder — ask the user or leave "TODO: Add description">
```

**Cell 2 — Code (setup):**
```python
# Install dependencies
%pip install anthropic python-dotenv

# Load environment variables from .env file
from dotenv import load_dotenv

# Create API client
from anthropic import Anthropic

client = Anthropic()
model = "claude-sonnet-4-6"
```

**Cell 3 - Helper functions**
```python
def add_user_message(messages, text):
    messages.append({"role": "user", "content": text})

def add_assistant_message(messages, text):
    messages.append({"role": "assistant", "content": text})

def chat(messages, system=None, temperature=0.5):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
        "temperature": temperature,
    }
    if system:
        params["system"] = system

    response = client.messages.create(**params)
    return response.content[0].text

messages = []


```

**Cell 4 — Empty code cell** ready for implementation.

3. Check if `.env` exists in that directory. If not, look for `.env` in any sibling section folder and copy it, or prompt the user to create one with `ANTHROPIC_API_KEY=sk-ant-...`.

4. If a `README.md` exists in the section folder, append an entry for the new notebook. If not, create a minimal one listing all notebooks in the folder.

**Important:** Generate valid `.ipynb` JSON (nbformat 4, nbformat_minor 5). Use `"metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}, "language_info": {"name": "python", "version": "3.13.3"}}` at notebook level.
