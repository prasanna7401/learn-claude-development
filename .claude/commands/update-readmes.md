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

## Step 3.5: Diff Against Existing READMEs

Before writing any README, read each existing section README and root README. Compare the current notebook inventory (from Steps 1-3) against what each README already documents:

1. **Identify changes:** Classify each notebook as:
   - **Unchanged** - present on disk AND already documented in the README with the same filename
   - **New** - present on disk but missing from the README
   - **Removed** - documented in the README but no longer on disk
   - **Renamed** - filename changed (old entry in README, new file on disk)

2. **Preserve existing content verbatim:**
   - For **section READMEs**: keep existing descriptions, key concepts, and all prose for unchanged notebooks exactly as written - do not rephrase, reword, or restructure them
   - For **root README**: keep existing summary text for unchanged notebooks exactly as written
   - Only generate new descriptions/summaries for notebooks classified as **new**
   - Remove entries for notebooks classified as **removed**
   - For **renamed** notebooks, update the filename/link but preserve the existing description

3. **Skip writing if no changes:** If a README's notebook inventory is identical to what is on disk (no new, removed, or renamed notebooks), do NOT rewrite the file at all.

## Step 4: Update Root `README.md`

Update the root `README.md` preserving existing content for unchanged notebooks. Use this structure:

```markdown
# learn-claude-development
Built with Claude API - For developers

## <N>. <Section Name (spaces)>

| # | Topic | Summary |
|---|-------|---------|
| <num> | [<Topic Name>](<section_dir>/<filename>) | <short summary ~120 chars> |
...

(repeat ## block for each section, in order)
```

Rules:
- Section heading uses the directory name with underscores replaced by spaces, prefixed by section number and a dot (e.g. `## 1. Claude API Basics`)
- Table rows use the notebook number (including sub-numbers like `7.1`), the topic name as a hyperlink to the notebook file (path relative to repo root, e.g. `[Making a Request](1_Claude_API_Basics/1_Making_request.ipynb)`), and the short summary
- No trailing blank lines between sections - just one blank line before each `##`
- Do NOT include any reference to `OTHERS/`

## Step 5: Update Section `README.md` Files

For each section, update `<section_dir>/README.md` preserving existing content for unchanged notebooks. Never rephrase existing descriptions or key concepts - only add entries for new notebooks and remove entries for deleted ones. Use this structure:

```markdown
# <Section Name (spaces)>

<One-line intro summarizing what this section covers.>

## Prerequisites

- Python 3.10+
- `anthropic` and `python-dotenv` packages
- An Anthropic API key in a `.env` file (`ANTHROPIC_API_KEY=sk-...`)

## Notebooks

### <N>. <Title>

<Long description - 1-2 sentences.>

**Key concepts:** <comma-separated list>

---

(repeat ### block for each notebook; omit `---` after the last one)
```

**Sub-numbered notebooks** (e.g. 7.1, 7.2) are grouped under a parent `###` heading:

```markdown
### <Parent#> <Parent Title>

#### <Sub#> <Sub Title>
<Long description>

**Key concepts:** <list>

#### <Sub#> <Sub Title>
<Long description>

**Key concepts:** <list>
```

No `---` separator between sub-notebooks under the same parent, but add `---` after the last sub-notebook before the next top-level `###`.

## Step 6: Verify

After writing all READMEs:

1. **Coverage check:** Confirm every `.ipynb` file in every section directory has a corresponding entry in both the root README table and the section README.
2. **No OTHERS references:** Grep all generated READMEs to confirm `OTHERS` does not appear anywhere.
3. **Link correctness:** Confirm all notebook links in the root README use paths relative to the repo root (e.g. `1_Claude_API_Basics/1_Making_request.ipynb`). Section READMEs should NOT contain notebook file links.
4. **Count match:** Confirm the total notebook count in the root README matches the sum across all section READMEs.

Report the results of these checks to the user.
