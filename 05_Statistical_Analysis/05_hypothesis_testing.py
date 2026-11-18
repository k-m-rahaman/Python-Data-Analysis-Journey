
"""
File: 05_hypothesis_testing.py
Topic: Hypothesis Testing

Description:
    Demonstrates one-sample and independent
    two-sample t-tests using SciPy.

Author: Kazi Mustafijur Rahaman
"""

import numpy as np
from scipy import stats


def one_sample_t_test():
    """Perform a one-sample t-test."""

    print("\n" + "=" * 55)
    print("ONE-SAMPLE T-TEST")
    print("=" * 55)

    # Student examination scores.

    scores = np.array([
        78, 82, 85, 74,
        80, 79, 88, 84,
        77, 81, 83, 76
    ])

    # Hypothesized population mean.

    hypothesized_mean = 75

    significance_level = 0.05

    # Perform t-test.

    result = stats.ttest_1samp(
        scores,
        popmean=hypothesized_mean
    )

    print("\nHYPOTHESES")

    print("H0: Population mean = 75")

    print("H1: Population mean != 75")

    print("\nRESULTS")

    print(f"Sample mean: {np.mean(scores):.4f}")

    print(f"T-statistic: {result.statistic:.4f}")

    print(f"P-value: {result.pvalue:.4f}")

    print(
        f"Significance level: {significance_level}"
    )

    # Decision.

    if result.pvalue < significance_level:

        print("\nDecision: Reject the null hypothesis.")

    else:

        print("\nDecision: Fail to reject the null hypothesis.")


def independent_t_test():
    """Compare two independent student groups."""

    print("\n" + "=" * 55)
    print("INDEPENDENT TWO-SAMPLE T-TEST")
    print("=" * 55)

    # Scores from two independent groups.

    group_a = np.array([
        72, 75, 78, 74,
        77, 76, 73, 79
    ])

    group_b = np.array([
        80, 82, 85, 78,
        84, 81, 83, 86
    ])

    significance_level = 0.05

    # Welch's independent t-test.

    result = stats.ttest_ind(
        group_a,
        group_b,
        equal_var=False
    )

    print("\nHYPOTHESES")

    print("H0: Both population means are equal.")

    print("H1: Both population means are different.")

    print("\nRESULTS")

    print(f"Group A mean: {np.mean(group_a):.3f}")

    print(f"Group B mean: {np.mean(group_b):.3f}")

    print(f"T-statistic: {result.statistic:.4f}")

    print(f"P-value: {result.pvalue:.4f}")

    # Decision.

    if result.pvalue < significance_level:

        print("\nDecision: Reject the null hypothesis.")

        print(
            "There is statistically significant "
            "evidence of a difference between the groups."
        )

    else:

        print("\nDecision: Fail to reject the null hypothesis.")

        print(
            "There is insufficient statistical evidence "
            "of a difference between the groups."
        )


def main():
    """Run all hypothesis testing demonstrations."""

    print("=" * 55)
    print("HYPOTHESIS TESTING")
    print("=" * 55)

    one_sample_t_test()

    independent_t_test()


if __name__ == "__main__":
    main()
