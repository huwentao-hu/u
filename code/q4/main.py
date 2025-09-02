from __future__ import annotations
import argparse
import random
from pathlib import Path

def generate_revised_fig(outdir: Path) -> None:
    """占位：生成改进策略图并保存为 outdir/"q4_revised_strategy.png"""
    # TODO: 实现绘图逻辑
    pass

def generate_effect_fig(outdir: Path) -> None:
    """占位：生成效果对比图并保存为 outdir/"q4_effect.png"""
    # TODO: 实现绘图逻辑
    pass

def main(outdir: str = "paper/figs", seed: int = 2025) -> None:
    path = Path(outdir)
    path.mkdir(parents=True, exist_ok=True)
    random.seed(seed)
    # TODO: 重新计算问题2和3在抽样误差下的策略
    generate_revised_fig(path)
    generate_effect_fig(path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=2025)
    parser.add_argument("--outdir", type=str, default="paper/figs")
    args = parser.parse_args()
    main(outdir=args.outdir, seed=args.seed)
