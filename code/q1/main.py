from __future__ import annotations

import argparse
import random
from pathlib import Path
from typing import Tuple

try:
    import numpy as np
    import matplotlib.pyplot as plt
except ModuleNotFoundError:  # pragma: no cover - 环境可能缺少依赖
    np = None
    plt = None
from math import gamma


def beta_pdf(x: np.ndarray, a: float, b: float) -> np.ndarray:
    """Beta 分布概率密度函数。"""
    B = gamma(a) * gamma(b) / gamma(a + b)
    return x ** (a - 1) * (1 - x) ** (b - 1) / B


def sequential_bayes(p_true: float, n: int, prior: Tuple[float, float]) -> Tuple[np.ndarray, np.ndarray, Tuple[float, float]]:
    """模拟序贯贝叶斯检验，返回样本、后验均值序列及最终参数。"""
    alpha, beta = prior
    samples = np.random.binomial(1, p_true, size=n)
    post_means = []
    for x in samples:
        alpha += x
        beta += 1 - x
        post_means.append(alpha / (alpha + beta))
    return samples, np.array(post_means), (alpha, beta)


def generate_convergence_fig(outdir: Path) -> None:
    """生成后验均值收敛曲线并保存为 q1_convergence.png。"""
    if np is None or plt is None:
        raise RuntimeError("需要 numpy 和 matplotlib 才能生成图像")
    _, means, _ = sequential_bayes(0.08, 120, (1.0, 1.0))
    plt.figure()
    plt.plot(range(1, len(means) + 1), means)
    plt.xlabel("样本数")
    plt.ylabel("后验均值")
    plt.title("次品率后验均值收敛")
    plt.savefig(outdir / "q1_convergence.png")
    plt.close()


def generate_posterior_fig(outdir: Path) -> None:
    """生成后验分布曲线并保存为 q1_posterior.png。"""
    if np is None or plt is None:
        raise RuntimeError("需要 numpy 和 matplotlib 才能生成图像")
    _, _, (a, b) = sequential_bayes(0.08, 120, (1.0, 1.0))
    xs = np.linspace(0, 0.2, 200)
    ys = beta_pdf(xs, a, b)
    plt.figure()
    plt.plot(xs, ys)
    plt.xlabel("次品率")
    plt.ylabel("概率密度")
    plt.title("次品率后验分布")
    plt.savefig(outdir / "q1_posterior.png")
    plt.close()


def generate_pred_fig(outdir: Path) -> None:
    """生成真实与预测次品率对比图并保存为 q1_pred.png。"""
    if np is None or plt is None:
        raise RuntimeError("需要 numpy 和 matplotlib 才能生成图像")
    _, _, (a, b) = sequential_bayes(0.08, 120, (1.0, 1.0))
    pred_mean = a / (a + b)
    plt.figure()
    plt.bar(["真实", "预测"], [0.08, pred_mean])
    plt.ylabel("次品率")
    plt.title("真实 vs. 后验预测")
    plt.savefig(outdir / "q1_pred.png")
    plt.close()


def main(outdir: str = "paper/figs", seed: int = 2025) -> None:
    path = Path(outdir)
    path.mkdir(parents=True, exist_ok=True)
    random.seed(seed)
    np.random.seed(seed)
    generate_convergence_fig(path)
    generate_posterior_fig(path)
    generate_pred_fig(path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=2025)
    parser.add_argument("--outdir", type=str, default="paper/figs")
    args = parser.parse_args()
    main(outdir=args.outdir, seed=args.seed)

