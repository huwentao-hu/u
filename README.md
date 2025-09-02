# CUMCM 建模 + 论文仓库（LaTeX 插图引入但不提交图片 · Codex Cloud · v5）

**目标：** 让 Codex 只编写 **LaTeX 代码**（含 `\includegraphics` 指向约定文件名），以及生成**图像生成代码骨架**；
但 **不在本仓库提交/生成任何图片或 PDF**，以便顺利创建 Pull Request。

- LaTeX 中 **正常使用** `\includegraphics{paper/figs/<name>.png}` 等语句；
- 图像文件名在 `reports/analysis/figures_manifest.md` 与 `reports/analysis/figspec.yaml` 中明确；
- `code/q*/main.py` 提供生成这些文件名的**代码骨架**（不执行）；
- `.gitignore` 已忽略图片/PDF 等二进制产物；
- 不包含 CI 编译流程（不产出 PDF）。

## 最短路径
1. 把赛题放到 `problem/problem.pdf`。
2. 在 ChatGPT 打开 **Codex** → 选 **Code** 模式，加载本仓库。
3. 将 `codex/codex_cloud_one_shot_prompt.txt` **整段粘贴**给 Codex：
   - 先抽题面到 `prompts/_inputs/statement.md`（纯文本）；
   - 再生成 `reports/analysis/*.md/.yaml`、`code/q*/` 骨架与 `paper/sections/*.tex`（含 `\includegraphics`）。

> 说明：未来需要出图时，只需在本地运行各 `code/q*/main.py` 生成图到 `paper/figs/`，再单独提交“二进制工件 PR”或发布 Release；**此仓库主 PR 保持纯文本**。