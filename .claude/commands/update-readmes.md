Regenerate all README files in this repository from the current notebook inventory.

## Step 1: Discover Sections

Scan the repository root for directories matching the pattern `<number>_<Name>/` (e.g. `1_Claude_API_Basics/`, `2_Prompt_Evaluation/`).

**Skip:** `OTHERS/`, `.claude/`, `.git/`, `node_modules/`, any dotfile directories, and any directory that does not start with a digit.

Sort sections by their leading number.

## Step 2: Inventory Notebooks

For each section directory, list all `.ipynb` files. Parse notebook numbers from the filename prefix (the part before the first `_`). Support sub-numbers like `7.1`, `7.2`.

Sort notebooks by their numeric prefix (e.g. 1, 2, 3, 4, 5, 6, 7.1, 7.2).

## Step 3: Extract Content from Each Notebook

Read each `.ipynb` file and extract:

- **Title:** from the first markdown cell's `# Heading` (strip the `# ` prefix). If no heading, derive from the filename.
- **Short summary:** ~120 characters, one-line description suitable for a table cell. Derive from the notebook's markdown cells and code cells.
- **Long description:** 1-2 sentences explaining what the notebook teaches. Pull from early markdown cells.
- **Key concepts:** a comma-separated list of the main API features, parameters, or patterns demonstrated. Look for bold terms, code references, and parameter names in both markdown and code cells.

## Step 4: Write Root `README.md`

Overwrite the root `README.md` with this exact structure:

```markdown
# learn-claude-development
Built with Claude API - For developers

## <N>. <Section Name (spaces)>

| # | Notebook | Summary |
|---|----------|---------|
| <num> | `<filename>` | <short summary ~120 chars> |
...

(repeat ## block for each section, in order)
```

Rules:
- Section heading uses the directory name with underscores replaced by spaces, prefixed by section number and a dot (e.g. `## 1. Claude API Basics`)
- Table rows use the notebook number (including sub-numbers like `7.1`), the filename in backticks, and the short summary
- No trailing blank lines between sections — just one blank line before each `##`
- Do NOT include any reference to `OTHERS/`

## Step 5: Write Section `README.md` Files

For each section, overwrite `<section_dir>/README.md` with this structure:

```markdown
# <Section Name (spaces)>

<One-line intro summarizing what this section covers.>

## Prerequisites

- Python 3.10+
- `anthropic` and `python-dotenv` packages
- An Anthropic API key in a `.env` file (`ANTHROPIC_API_KEY=sk-...`)

## Notebooks

### <N>. <Title>
[`<filename>`](<filename>)

<Long description — 1-2 sentences.>

**Key concepts:** <comma-separated list>

---

(repeat ### block for each notebook; omit `---` after the last one)
```

**Sub-numbered notebooks** (e.g. 7.1, 7.2) are grouped under a parent `###` heading:

```markdown
### <Parent#> <Parent Title>

#### <Sub#> <Sub Title>
[`<filename>`](<filename>)

<Long description>

**Key concepts:** <list>

#### <Sub#> <Sub Title>
[`<filename>`](<filename>)

<Long description>

**Key concepts:** <list>
```

No `---` separator between sub-notebooks under the same parent, but add `---` after the last sub-notebook before the next top-level `###`.

## Step 6: Verify

After writing all READMEs:

1. **Coverage check:** Confirm every `.ipynb` file in every section directory has a corresponding entry in both the root README table and the section README.
2. **No OTHERS references:** Grep all generated READMEs to confirm `OTHERS` does not appear anywhere.
3. **Link correctness:** Confirm all notebook links in section READMEs use the bare filename (relative link within the same directory), not absolute paths.
4. **Count match:** Confirm the total notebook count in the root README matches the sum across all section READMEs.

Report the results of these checks to the user.
