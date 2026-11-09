"""
File: 01_arrays.py
Topic: NumPy Array Fundamentals

Description:
    Demonstrates NumPy array creation, dimensions,
    shapes, data types, reshaping, and basic operations.

Author: Kazi Mustafijur Rahaman
"""

import numpy as np


def demonstrate_array_basics() -> None:
    """Create 1D, 2D, and 3D arrays and inspect their properties."""

    # One-dimensional array
    student_scores = np.array(
        [78, 85, 90, 66],
        dtype=np.int64
    )

    # Two-dimensional array
    class_marks = np.array([
        [78, 85, 90],
        [72, 88, 91]
    ])

    # Three-dimensional array
    data_cube = np.arange(1, 9).reshape(2, 2, 2)

    print("=== Array Basics ===")

    print("1D scores:", student_scores)

    print(
        "2D marks:\n",
        class_marks,
        sep=""
    )

    print("3D array shape:", data_cube.shape)

    # Important array properties
    print("Dimensions:", class_marks.ndim)
    print("Shape:", class_marks.shape)
    print("Total elements:", class_marks.size)
    print("Data type:", student_scores.dtype)


def demonstrate_array_creation() -> None:
    """Create arrays using NumPy's built-in functions."""

    print("\n=== Array Creation ===")

    # Even numbers from 2 through 10
    print(
        "Even numbers:",
        np.arange(2, 11, 2)
    )

    # Equally spaced values
    print(
        "Five equally spaced values:",
        np.linspace(0, 1, 5)
    )

    # Array containing zeros
    print(
        "Zeros:\n",
        np.zeros((2, 3), dtype=int),
        sep=""
    )

    # Array containing ones
    print(
        "Ones:\n",
        np.ones((2, 2), dtype=int),
        sep=""
    )

    # Array filled with a constant
    print(
        "Constant values:",
        np.full(4, 7)
    )

    # Identity matrix
    print(
        "Identity matrix:\n",
        np.eye(3, dtype=int),
        sep=""
    )

    # Reshape an existing array
    scores = np.array([78, 85, 90, 66])

    print(
        "Reshaped scores:\n",
        scores.reshape(2, 2),
        sep=""
    )

    # Change the data type
    print(
        "Converted to float:",
        scores.astype(float)
    )

    # Reproducible random number generation
    generator = np.random.default_rng(42)

    random_numbers = generator.integers(
        1,
        10,
        size=5
    )

    print(
        "Reproducible random integers:",
        random_numbers
    )


def main() -> None:
    """Execute the introductory NumPy demonstrations."""

    demonstrate_array_basics()
    demonstrate_array_creation()


if __name__ == "__main__":
    main()