from __future__ import annotations

import argparse
import random
from pathlib import Path
from typing import Tuple

try:
    import numpy as np
    import matplotlib.pyplot as plt
except ModuleNotFoundError:  # pragma: no cover
    np = None
    plt = None


def value_iteration(cost_inspect: Tuple[float, float], cost_defect: float,
                   p1: float, p2: float, gamma: float = 0.95,
                   iterations: int = 50) -> Tuple[np.ndarray, np.ndarray]:
    """简单价值迭代，返回状态价值与策略矩阵。"""
    V = np.zeros((2, 2))
    policy = np.zeros((2, 2), dtype=int)
    for _ in range(iterations):
        for i in range(2):
            for j in range(2):
                vals = []
                for a in range(4):  # 0: none, 1: inspect1, 2: inspect2, 3: both
                    c = 0.0
                    if a in (1, 3):
                        c += cost_inspect[0]
                    if a in (2, 3):
                        c += cost_inspect[1]
                    if a not in (1, 3):
                        c += (p1 if i == 1 else 0) * cost_defect
                    if a not in (2, 3):
                        c += (p2 if j == 1 else 0) * cost_defect
                    vals.append(c + gamma * V[0, 0])
                best = np.min(vals)
                policy[i, j] = int(np.argmin(vals))
                V[i, j] = best
    return V, policy


def generate_sensitivity_fig(outdir: Path) -> None:
    """生成检测成本敏感性图。"""
    if np is None or plt is None:
        raise RuntimeError("需要 numpy 和 matplotlib 才能生成图像")
    multipliers = np.linspace(0.5, 1.5, 20)
    costs = []
    for m in multipliers:
        V, _ = value_iteration((m * 1.0, m * 1.2), 5.0, 0.1, 0.15)
        costs.append(V[1, 1])
    plt.figure()
    plt.plot(multipliers, costs)
    plt.xlabel("检测成本倍数")
    plt.ylabel("期望成本")
    plt.title("检测成本敏感性")
    plt.savefig(outdir / "q2_sensitivity.png")
    plt.close()


def generate_ablation_fig(outdir: Path) -> None:
    """生成消融对比图。"""
    if np is None or plt is None:
        raise RuntimeError("需要 numpy 和 matplotlib 才能生成图像")
    full, _ = value_iteration((1.0, 1.2), 5.0, 0.1, 0.15)
    no1, _ = value_iteration((0.0, 1.2), 5.0, 0.1, 0.15)
    no2, _ = value_iteration((1.0, 0.0), 5.0, 0.1, 0.15)
    vals = [full[1, 1], no1[1, 1], no2[1, 1]]
    plt.figure()
    plt.bar(["全策略", "无检1", "无检2"], vals)
    plt.ylabel("期望成本")
    plt.title("检测策略消融")
    plt.savefig(outdir / "q2_ablation.png")
    plt.close()


def generate_policy_fig(outdir: Path) -> None:
    """绘制最优策略热力图。"""
    if np is None or plt is None:
        raise RuntimeError("需要 numpy 和 matplotlib 才能生成图像")
    _, policy = value_iteration((1.0, 1.2), 5.0, 0.1, 0.15)
    plt.figure()
    plt.imshow(policy, cmap="viridis", origin="lower")
    plt.colorbar(label="动作编码")
    plt.xlabel("零件2状态")
    plt.ylabel("零件1状态")
    plt.title("最优策略热力图")
    plt.savefig(outdir / "q2_policy.png")
    plt.close()


def main(outdir: str = "paper/figs", seed: int = 2025) -> None:
    path = Path(outdir)
    path.mkdir(parents=True, exist_ok=True)
    random.seed(seed)
    if np is not None:
        np.random.seed(seed)
    generate_sensitivity_fig(path)
    generate_ablation_fig(path)
    generate_policy_fig(path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=2025)
    parser.add_argument("--outdir", type=str, default="paper/figs")
    args = parser.parse_args()
    main(outdir=args.outdir, seed=args.seed)

