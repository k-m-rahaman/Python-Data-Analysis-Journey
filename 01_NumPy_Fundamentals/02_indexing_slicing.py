"""
File: 02_indexing_slicing.py
Topic: NumPy Indexing and Slicing

Description:
    Demonstrates positive and negative indexing,
    slicing, multidimensional indexing, boolean
    filtering, fancy indexing, and memory behavior.

Author: Kazi Mustafijur Rahaman
"""

import numpy as np


def demonstrate_indexing() -> None:
    """Access elements and slices from 1D and 2D arrays."""

    values = np.array([
        10, 20, 30, 40, 50, 60
    ])

    matrix = np.array([
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]
    ])

    print("=== 1D Indexing and Slicing ===")

    # Positive indexing
    print("First element:", values[0])

    # Negative indexing
    print("Last element:", values[-1])

    # Access elements with a step
    print(
        "Every second element:",
        values[::2]
    )

    # Slice a specific range
    print(
        "Values from index 1 to 4:",
        values[1:5]
    )

    # Reverse an array
    print(
        "Reversed array:",
        values[::-1]
    )

    print("\n=== 2D Indexing and Slicing ===")

    # Access a specific row and column
    print(
        "Element at row 2, column 3:",
        matrix[1, 2]
    )

    # Select an entire row
    print(
        "Second row:",
        matrix[1, :]
    )

    # Select an entire column
    print(
        "Third column:",
        matrix[:, 2]
    )

    # Select a submatrix
    print(
        "Top-left 2x2 block:\n",
        matrix[:2, :2],
        sep=""
    )


def demonstrate_advanced_indexing() -> None:
    """Demonstrate boolean filtering and fancy indexing."""

    scores = np.array([
        62, 85, 73, 94, 58, 88
    ])

    print("\n=== Advanced Indexing ===")

    # Boolean indexing
    high_scores = scores[scores >= 80]

    print(
        "Scores >= 80:",
        high_scores
    )

    # Fancy indexing
    selected_scores = scores[[0, 2, 4]]

    print(
        "First, third, fifth scores:",
        selected_scores
    )

    # Count elements satisfying a condition
    count = np.count_nonzero(scores >= 80)

    print(
        "Number of scores >= 80:",
        count
    )


def demonstrate_views_and_copies() -> None:
    """Explain the difference between views and independent copies."""

    original = np.array([10, 20, 30, 40])

    # Basic slicing normally creates a view
    view = original[1:3]

    # Modifying the view changes the original
    view[0] = 99

    # An explicit copy stores independent data
    independent_copy = original[1:3].copy()

    independent_copy[0] = -5

    print("\n=== Views vs Copies ===")

    print(
        "Original after modifying view:",
        original
    )

    print(
        "Independent copy:",
        independent_copy
    )

    print(
        "Original unchanged by copy edit:",
        original
    )

    # Handle an invalid index
    try:
        _ = original[100]

    except IndexError:
        print(
            "Out-of-range indexing safely handled."
        )


def main() -> None:
    """Run indexing and slicing examples."""

    demonstrate_indexing()
    demonstrate_advanced_indexing()
    demonstrate_views_and_copies()


if __name__ == "__main__":
    main()