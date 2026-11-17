
"""
File: 02_probability_distributions.py
Topic: Probability Distributions

Description:
    Demonstrates binomial and normal distributions
    using SciPy and visualizes their behavior.

Author: Kazi Mustafijur Rahaman
"""

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import binom, norm


def analyze_distributions():
    """Analyze binomial and normal distributions."""

    print("=" * 55)
    print("PROBABILITY DISTRIBUTIONS")
    print("=" * 55)

    # 1. Binomial Distribution

    trials = 10
    probability = 0.5

    probability_exactly_five = binom.pmf(
        5, trials, probability
    )

    probability_at_most_two = binom.cdf(
        2, trials, probability
    )

    print("\nBINOMIAL DISTRIBUTION")

    print(
        "Probability of exactly 5 successes:",
        f"{probability_exactly_five:.4f}"
    )

    print(
        "Probability of at most 2 successes:",
        f"{probability_at_most_two:.4f}"
    )

    # 2. Normal Distribution

    mean = 70
    standard_deviation = 10

    probability_between = (
        norm.cdf(80, mean, standard_deviation)
        - norm.cdf(60, mean, standard_deviation)
    )

    z_score = (
        (85 - mean) / standard_deviation
    )

    print("\nNORMAL DISTRIBUTION")

    print(
        "Probability between 60 and 80:",
        f"{probability_between:.4f}"
    )

    print(
        "Z-score for value 85:",
        f"{z_score:.2f}"
    )

    # 3. Create visualizations

    output_dir = (
        Path(__file__).resolve().parent / "outputs"
    )

    output_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    fig, axes = plt.subplots(
        1, 2, figsize=(12, 5)
    )

    # Binomial PMF

    x_binomial = np.arange(0, trials + 1)

    y_binomial = binom.pmf(
        x_binomial,
        trials,
        probability
    )

    axes[0].bar(
        x_binomial,
        y_binomial,
        color="steelblue"
    )

    axes[0].set_title("Binomial Distribution")
    axes[0].set_xlabel("Number of Successes")
    axes[0].set_ylabel("Probability")

    # Normal PDF

    x_normal = np.linspace(40, 100, 300)

    y_normal = norm.pdf(
        x_normal,
        mean,
        standard_deviation
    )

    axes[1].plot(
        x_normal,
        y_normal,
        color="darkorange",
        linewidth=2
    )

    axes[1].set_title("Normal Distribution")
    axes[1].set_xlabel("Values")
    axes[1].set_ylabel("Probability Density")

    fig.tight_layout()

    fig.savefig(
        output_dir / "01_probability_distributions.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()
    plt.close(fig)

    print("\nVisualization saved successfully!")


if __name__ == "__main__":
    analyze_distributions()
