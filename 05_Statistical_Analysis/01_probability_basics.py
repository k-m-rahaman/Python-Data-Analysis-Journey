
"""
File: 01_probability_basics.py
Topic: Probability Fundamentals

Description:
    Demonstrates basic probability calculations
    using dice and coin toss experiments.

Author: Kazi Mustafijur Rahaman
"""

from itertools import product


def calculate_probability(favorable, total):
    """Calculate the probability of an event."""

    return favorable / total


def demonstrate_probability():
    """Demonstrate basic probability concepts."""

    print("=" * 55)
    print("PROBABILITY FUNDAMENTALS")
    print("=" * 55)

    # 1. Dice experiment

    dice_outcomes = list(range(1, 7))

    even_outcomes = [
        value for value in dice_outcomes
        if value % 2 == 0
    ]

    greater_than_four = [
        value for value in dice_outcomes
        if value > 4
    ]

    print("\nDICE EXPERIMENT")

    print("Sample space:", dice_outcomes)

    probability_even = calculate_probability(
        len(even_outcomes),
        len(dice_outcomes)
    )

    print(
        f"Probability of an even number: "
        f"{probability_even:.4f}"
    )

    probability_greater = calculate_probability(
        len(greater_than_four),
        len(dice_outcomes)
    )

    print(
        f"Probability of number greater than 4: "
        f"{probability_greater:.4f}"
    )

    # 2. Union of events

    union_outcomes = set(even_outcomes) | set(
        greater_than_four
    )

    probability_union = calculate_probability(
        len(union_outcomes),
        len(dice_outcomes)
    )

    print(
        f"Probability of even OR greater than 4: "
        f"{probability_union:.4f}"
    )

    # 3. Coin toss experiment

    coin_outcomes = list(
        product(["H", "T"], repeat=2)
    )

    exactly_one_head = [
        outcome for outcome in coin_outcomes
        if outcome.count("H") == 1
    ]

    two_heads = [
        outcome for outcome in coin_outcomes
        if outcome.count("H") == 2
    ]

    print("\nCOIN TOSS EXPERIMENT")

    print("Sample space:", coin_outcomes)

    print(
        "Probability of exactly one head:",
        f"{calculate_probability(len(exactly_one_head), len(coin_outcomes)):.4f}"
    )

    print(
        "Probability of two heads:",
        f"{calculate_probability(len(two_heads), len(coin_outcomes)):.4f}"
    )


if __name__ == "__main__":
    demonstrate_probability()
