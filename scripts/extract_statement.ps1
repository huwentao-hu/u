Param(
  [string]$InputPdf = "problem/problem.pdf",
  [string]$OutputMd = "prompts/_inputs/statement.md"
)
# 需要提前: pip install pdfminer.six
$py = @'
from pdfminer.high_level import extract_text
from pathlib import Path
inp = Path(r + ${InputPdf} + r)
outp = Path(r + ${OutputMd} + r)
outp.parent.mkdir(parents=True, exist_ok=True)
text = extract_text(str(inp)) if inp.exists() else "# 请先把题面 PDF 放到 problem/problem.pdf"
outp.write_text(text, encoding="utf-8")
print(f"Wrote {outp}")
'@
python - <<PY
$py
PY