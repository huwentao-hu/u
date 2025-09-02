from __future__ import annotations
import argparse
import random
from pathlib import Path

def generate_convergence_fig(outdir: Path) -> None:
    """占位：生成收敛曲线并保存为 outdir/"q1_convergence.png"""
    # TODO: 实现具体绘图逻辑
    pass

def generate_pred_fig(outdir: Path) -> None:
    """占位：生成真实-预测对比图并保存为 outdir/"q1_pred.png"""
    # TODO: 实现具体绘图逻辑
    pass

def main(outdir: str = "paper/figs", seed: int = 2025) -> None:
    path = Path(outdir)
    path.mkdir(parents=True, exist_ok=True)
    random.seed(seed)
    # TODO: 使用随机数生成/载入数据，拟合与评估
    generate_convergence_fig(path)
    generate_pred_fig(path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=2025)
    parser.add_argument("--outdir", type=str, default="paper/figs")
    args = parser.parse_args()
    main(outdir=args.outdir, seed=args.seed)
