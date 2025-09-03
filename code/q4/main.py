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


def sample_defect_rate(true_p: float, n: int,
                       alpha0: float = 1.0, beta0: float = 1.0) -> float:
    """基于抽样数据的贝叶斯估计，返回次品率样本。"""
    if np is None:
        raise RuntimeError("需要 numpy 才能进行抽样")
    sample = np.random.binomial(1, true_p, size=n)
    a = alpha0 + sample.sum()
    b = beta0 + n - sample.sum()
    return np.random.beta(a, b)


def simulate_policy(p_hat: float, policy: str, n_runs: int = 1000) -> np.ndarray:
    """根据估计次品率模拟策略成本分布。"""
    if np is None:
        raise RuntimeError("需要 numpy 才能进行模拟")
    costs = []
    for _ in range(n_runs):
        defect = np.random.rand() < p_hat
        if policy == "baseline":
            c = 5.0 if defect else 0.0
        else:  # robust policy: always inspect with cost 1, reduces defect loss
            c = 1.0 + (3.0 if defect else 0.0)
        costs.append(c)
    return np.array(costs)


def cvar(costs: np.ndarray, alpha: float) -> float:
    """计算条件在险价值。"""
    if np is None:
        raise RuntimeError("需要 numpy 才能计算风险")
    sorted_costs = np.sort(costs)
    k = int(np.ceil(alpha * len(sorted_costs)))
    return sorted_costs[:k].mean()


def generate_revised_strategy_fig(outdir: Path) -> None:
    """绘制改进策略流程示意图。"""
    if plt is None:
        raise RuntimeError("需要 matplotlib 才能生成图像")
    plt.figure()
    plt.text(0.1, 0.8, "抽样", fontsize=12)
    plt.text(0.4, 0.8, "贝叶斯更新", fontsize=12)
    plt.text(0.7, 0.8, "鲁棒决策", fontsize=12)
    plt.arrow(0.2, 0.82, 0.15, 0, head_width=0.03)
    plt.arrow(0.5, 0.82, 0.15, 0, head_width=0.03)
    plt.axis("off")
    plt.savefig(outdir / "q4_revised_strategy.png")
    plt.close()


def generate_effect_fig(outdir: Path) -> None:
    """生成基准策略与鲁棒策略的成本对比图。"""
    if np is None or plt is None:
        raise RuntimeError("需要 numpy 和 matplotlib 才能生成图像")
    p_hat = sample_defect_rate(0.08, 30)
    base = simulate_policy(p_hat, "baseline").mean()
    robust = simulate_policy(p_hat, "robust").mean()
    plt.figure()
    plt.bar(["基准", "鲁棒"], [base, robust])
    plt.ylabel("平均成本")
    plt.title("策略成本对比")
    plt.savefig(outdir / "q4_effect.png")
    plt.close()


def generate_risk_fig(outdir: Path) -> None:
    """绘制鲁棒策略在不同置信水平下的 CVaR。"""
    if np is None or plt is None:
        raise RuntimeError("需要 numpy 和 matplotlib 才能生成图像")
    p_hat = sample_defect_rate(0.08, 30)
    costs = simulate_policy(p_hat, "robust")
    alphas = np.linspace(0.8, 0.99, 20)
    risks = [cvar(costs, a) for a in alphas]
    plt.figure()
    plt.plot(alphas, risks)
    plt.xlabel("置信水平 α")
    plt.ylabel("CVaR")
    plt.title("鲁棒策略风险曲线")
    plt.savefig(outdir / "q4_risk.png")
    plt.close()


def main(outdir: str = "paper/figs", seed: int = 2025) -> None:
    path = Path(outdir)
    path.mkdir(parents=True, exist_ok=True)
    random.seed(seed)
    if np is not None:
        np.random.seed(seed)
    generate_revised_strategy_fig(path)
    generate_effect_fig(path)
    generate_risk_fig(path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=2025)
    parser.add_argument("--outdir", type=str, default="paper/figs")
    args = parser.parse_args()
    main(outdir=args.outdir, seed=args.seed)

