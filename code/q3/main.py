from __future__ import annotations
import argparse
import random
from pathlib import Path

def generate_strategy_fig(outdir: Path) -> None:
    """占位：生成决策流程图并保存为 outdir/"q3_strategy.png"""
    # TODO: 实现绘图逻辑
    pass

def generate_cost_fig(outdir: Path) -> None:
    """占位：生成成本比较图并保存为 outdir/"q3_cost.png"""
    # TODO: 实现绘图逻辑
    pass

def main(outdir: str = "paper/figs", seed: int = 2025) -> None:
    path = Path(outdir)
    path.mkdir(parents=True, exist_ok=True)
    random.seed(seed)
    # TODO: 模拟生产与决策过程
    generate_strategy_fig(path)
    generate_cost_fig(path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=2025)
    parser.add_argument("--outdir", type=str, default="paper/figs")
    args = parser.parse_args()
    main(outdir=args.outdir, seed=args.seed)
