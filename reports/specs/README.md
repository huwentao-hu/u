# Repo Specs（插图策略）

- LaTeX 论文**直接写** `\includegraphics{paper/figs/<name>.png}`。
- 代码骨架（code/q*/main.py）负责**将来**生成这些文件名的图片。
- 本仓库 PR 不提交图片/ PDF（二进制文件），已在 `.gitignore` 忽略。
- 如确需在未生成图片时进行编译测试，可临时把 `\includegraphics` 改为 `\safeincludegraphics`。