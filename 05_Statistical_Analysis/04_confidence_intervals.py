
"""
File: 04_confidence_intervals.py
Topic: Confidence Intervals

Description:
    Calculates a confidence interval for a population
    mean using sample data and the Student's t-distribution.

Author: Kazi Mustafijur Rahaman
"""

import numpy as np
from scipy import stats


def calculate_confidence_interval():
    """Calculate a 95% confidence interval."""

    print("=" * 55)
    print("CONFIDENCE INTERVAL ANALYSIS")
    print("=" * 55)

    # Sample examination scores.

    scores = np.array([
        72, 75, 78, 80,
        82, 85, 88, 90,
        76, 79, 83, 87
    ], dtype=float)

    # 1. Sample information.

    sample_size = len(scores)

    sample_mean = np.mean(scores)

    sample_std = np.std(
        scores,
        ddof=1
    )

    # 2. Standard error.

    standard_error = stats.sem(scores)

    # 3. Confidence level.

    confidence_level = 0.95

    alpha = 1 - confidence_level

    degrees_of_freedom = sample_size - 1

    # 4. Critical t-value.

    critical_value = stats.t.ppf(
        1 - alpha / 2,
        degrees_of_freedom
    )

    # 5. Margin of error.

    margin_of_error = (
        critical_value * standard_error
    )

    # 6. Calculate confidence interval.

    lower_bound = (
        sample_mean - margin_of_error
    )

    upper_bound = (
        sample_mean + margin_of_error
    )

    # Display results.

    print("\nSAMPLE INFORMATION")

    print(f"Sample size: {sample_size}")

    print(f"Sample mean: {sample_mean:.2f}")

    print(f"Sample standard deviation: {sample_std:.2f}")

    print(f"Standard error: {standard_error:.2f}")

    print("\nCONFIDENCE INTERVAL")

    print(f"Confidence level: {confidence_level * 100:.0f}%")

    print(f"Critical t-value: {critical_value:.2f}")

    print(f"Margin of error: {margin_of_error:.2f}")

    print(
        f"\nLower bound: {lower_bound:.2f}"
    )

    print(
        f"Upper bound: {upper_bound:.2f}"
    )

    print(
        f"\n95% Confidence Interval: "
        f"({lower_bound:.2f}, {upper_bound:.2f})"
    )


if __name__ == "__main__":
    calculate_confidence_interval()
