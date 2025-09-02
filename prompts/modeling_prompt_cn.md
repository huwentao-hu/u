# 数模国赛——建模提示词（含图像文件名约定）

- 逐句拆题：背景/核心问题/已知/约束四列表；小问“直接/隐含目标”；依赖要点；题型分类（100–150字）。
- 每小问双方案：基础适配 × 创新融合；原理/适配性/创新点/局限/判定流程。
- 变量—假设—公式—流程：变量表；3–5 条可检验/可放松假设；目标与约束推导及物理含义。
- 求解与检验：文本 + 公式描述；**图像文件名按 `paper/figs/q{问号}_<主题>.png` 约定**，在 LaTeX 中 `\includegraphics` 引用，具体清单写入 figures_manifest 与 figspec.yaml。

> 示例：
> - Q1：q1_convergence.png / q1_pred.png
> - Q2：q2_sensitivity.png / q2_ablation.png