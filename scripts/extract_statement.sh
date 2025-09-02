#!/usr/bin/env bash
set -euo pipefail

mkdir -p prompts/_inputs
python - <<'PY'
from pdfminer.high_level import extract_text
from pathlib import Path
inp = Path('problem/problem.pdf')
outp = Path('prompts/_inputs/statement.md')
outp.parent.mkdir(parents=True, exist_ok=True)
text = extract_text(str(inp)) if inp.exists() else "# 请先把题面 PDF 放到 problem/problem.pdf"
outp.write_text(text, encoding='utf-8')
print(f"Wrote {outp}")
PY