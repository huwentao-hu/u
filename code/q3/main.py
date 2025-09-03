from __future__ import annotations

import argparse
import random
from pathlib import Path

try:
    import numpy as np
    import matplotlib.pyplot as plt
except ModuleNotFoundError:  # pragma: no cover
    np = None
    plt = None


def simulate_cost(n_runs: int, cost_detect: float, cost_disassemble: float,
                  p1: float, p2: float) -> np.ndarray:
    """蒙特卡洛模拟单批次生产的成本分布。"""
    if np is None:
        raise RuntimeError("需要 numpy 才能进行模拟")
    costs = []
    for _ in range(n_runs):
        defect1 = np.random.rand() < p1
        defect2 = np.random.rand() < p2
        c = 0.0
        if defect1 or defect2:
            c += cost_detect
            if defect1 and defect2:
                c += cost_disassemble
        costs.append(c)
    return np.array(costs)


def generate_strategy_fig(outdir: Path) -> None:
    """生成决策流程示意图。"""
    if plt is None:
        raise RuntimeError("需要 matplotlib 才能生成图像")
    plt.figure()
    plt.text(0.1, 0.8, "采购", fontsize=12)
    plt.text(0.4, 0.8, "检测", fontsize=12)
    plt.text(0.7, 0.8, "装配", fontsize=12)
    plt.text(0.4, 0.4, "拆解", fontsize=12)
    plt.arrow(0.2, 0.82, 0.15, 0, head_width=0.03)
    plt.arrow(0.5, 0.82, 0.15, 0, head_width=0.03)
    plt.arrow(0.4, 0.78, 0, -0.28, head_width=0.03)
    plt.arrow(0.42, 0.42, 0.25, 0, head_width=0.03)
    plt.axis("off")
    plt.savefig(outdir / "q3_strategy.png")
    plt.close()


def generate_cost_fig(outdir: Path) -> None:
    """生成不同策略的平均成本对比图。"""
    if np is None or plt is None:
        raise RuntimeError("需要 numpy 和 matplotlib 才能生成图像")
    base = simulate_cost(1000, 1.0, 2.0, 0.1, 0.15).mean()
    improved = simulate_cost(1000, 0.8, 1.5, 0.1, 0.15).mean()
    plt.figure()
    plt.bar(["基准", "改进"], [base, improved])
    plt.ylabel("平均成本")
    plt.title("策略成本对比")
    plt.savefig(outdir / "q3_cost.png")
    plt.close()


def generate_cost_distribution_fig(outdir: Path) -> None:
    """生成成本分布直方图。"""
    if np is None or plt is None:
        raise RuntimeError("需要 numpy 和 matplotlib 才能生成图像")
    costs = simulate_cost(1000, 1.0, 2.0, 0.1, 0.15)
    plt.figure()
    plt.hist(costs, bins=20)
    plt.xlabel("成本")
    plt.ylabel("频数")
    plt.title("成本分布")
    plt.savefig(outdir / "q3_cost_dist.png")
    plt.close()


def main(outdir: str = "paper/figs", seed: int = 2025) -> None:
    path = Path(outdir)
    path.mkdir(parents=True, exist_ok=True)
    random.seed(seed)
    if np is not None:
        np.random.seed(seed)
    generate_strategy_fig(path)
    generate_cost_fig(path)
    generate_cost_distribution_fig(path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=2025)
    parser.add_argument("--outdir", type=str, default="paper/figs")
    args = parser.parse_args()
    main(outdir=args.outdir, seed=args.seed)

