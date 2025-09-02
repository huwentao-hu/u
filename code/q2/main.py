from pathlib import Path

def generate_sensitivity_fig(outdir: Path):
    # TODO: 生成参数敏感性图并保存为 outdir/"q2_sensitivity.png"
    pass

def generate_ablation_fig(outdir: Path):
    # TODO: 生成消融对比图并保存为 outdir/"q2_ablation.png"
    pass

def main(outdir: str = "paper/figs", seed: int = 2025):
    Path(outdir).mkdir(parents=True, exist_ok=True)
    # TODO: 载入数据/设置实验，输出图片到指定文件名
    generate_sensitivity_fig(Path(outdir))
    generate_ablation_fig(Path(outdir))

if __name__ == "__main__":
    main()