from pathlib import Path

def generate_convergence_fig(outdir: Path):
    # TODO: 生成收敛曲线并保存为 outdir/"q1_convergence.png"
    pass

def generate_pred_fig(outdir: Path):
    # TODO: 生成真实-预测对比图并保存为 outdir/"q1_pred.png"
    pass

def main(outdir: str = "paper/figs", seed: int = 2025):
    Path(outdir).mkdir(parents=True, exist_ok=True)
    # TODO: 设置随机种子，载入/合成数据，拟合与评估
    generate_convergence_fig(Path(outdir))
    generate_pred_fig(Path(outdir))

if __name__ == "__main__":
    # TODO: 解析 CLI 参数（--seed, --data, --outdir）
    main()