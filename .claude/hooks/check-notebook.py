"""
Post-edit hook: checks Jupyter notebooks for common issues.

Usage: python check-notebook.py <path-to-notebook.ipynb>

Exits 0 with warnings printed to stderr (non-blocking).
"""

import json
import re
import sys
from pathlib import Path


def check_notebook(path: str) -> list[str]:
    nb_path = Path(path)
    if not nb_path.exists() or nb_path.suffix != ".ipynb":
        return []

    try:
        nb = json.loads(nb_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError):
        return [f"WARNING: {path} is not valid JSON"]

    cells = nb.get("cells", [])
    if not cells:
        return [f"WARNING: {path} has no cells"]

    warnings = []
    all_code = ""
    code_cells = [c for c in cells if c.get("cell_type") == "code"]

    for cell in code_cells:
        source = "".join(cell.get("source", []))
        all_code += source + "\n"

    # Check 1: pip install in first code cell
    if code_cells:
        first_source = "".join(code_cells[0].get("source", []))
        if "%pip install" not in first_source and "!pip install" not in first_source:
            warnings.append(
                f"WARNING: {path} — first code cell missing '%pip install anthropic python-dotenv'"
            )

    # Check 2: dotenv import and load
    if "load_dotenv" not in all_code:
        warnings.append(
            f"WARNING: {path} — missing 'load_dotenv()' call"
        )
    if "from dotenv" not in all_code and "import dotenv" not in all_code:
        warnings.append(
            f"WARNING: {path} — missing dotenv import"
        )

    # Check 3: Hardcoded API keys
    if re.search(r"sk-ant-[a-zA-Z0-9_-]{10,}", all_code):
        warnings.append(
            f"CRITICAL: {path} — hardcoded API key detected (sk-ant-...)! Use .env instead"
        )

    # Check 4: Model variable
    if "model" not in all_code and "MODEL" not in all_code:
        warnings.append(
            f"WARNING: {path} — no 'model' variable defined; consider defining one for consistency"
        )

    return warnings


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python check-notebook.py <notebook.ipynb>", file=sys.stderr)
        sys.exit(0)

    path = sys.argv[1]
    if not path.endswith(".ipynb"):
        sys.exit(0)

    warnings = check_notebook(path)
    if warnings:
        for w in warnings:
            print(w, file=sys.stderr)
        # Exit 1 only for CRITICAL issues (hardcoded keys)
        if any("CRITICAL" in w for w in warnings):
            sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()
