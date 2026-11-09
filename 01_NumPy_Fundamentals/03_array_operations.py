"""
File: 03_array_operations.py
Topic: NumPy Mathematical and Statistical Operations

Description:
    Demonstrates vectorized arithmetic, mathematical
    functions, aggregation, filtering, safe division,
    and Z-score normalization.

Author: Kazi Mustafijur Rahaman
"""

import numpy as np


def z_score(values: np.ndarray) -> np.ndarray:
    """
    Standardize numeric values using Z-score normalization.

    Formula:
        z = (x - mean) / standard_deviation

    Constant arrays are converted to arrays of zeros.
    """

    numbers = np.asarray(values, dtype=float)

    # Validate the input
    if numbers.size == 0 or not np.all(np.isfinite(numbers)):
        raise ValueError(
            "Expected a nonempty array of finite numeric values."
        )

    standard_deviation = numbers.std()

    # Avoid division by zero
    if np.isclose(standard_deviation, 0.0):
        return np.zeros_like(numbers)

    return (
        numbers - numbers.mean()
    ) / standard_deviation


def demonstrate_arithmetic() -> None:
    """Perform vectorized mathematical operations."""

    first = np.array([10, 20, 30, 40])
    second = np.array([1, 2, 3, 4])

    print("=== Vectorized Operations ===")

    print("Addition:", first + second)
    print("Subtraction:", first - second)
    print("Multiplication:", first * second)
    print("Division:", first / second)

    # Exponentiation
    print("Squared:", second**2)

    # Square roots
    print(
        "Square roots:",
        np.sqrt([4, 9, 16])
    )

    # Safe division with zero denominators
    numerator = np.array([
        10.0, 20.0, 30.0
    ])

    denominator = np.array([
        2.0, 0.0, 5.0
    ])

    safe_result = np.divide(
        numerator,
        denominator,
        out=np.full(numerator.shape, np.nan),
        where=denominator != 0
    )

    print(
        "Safe division (undefined = NaN):",
        safe_result
    )


def demonstrate_statistics() -> None:
    """Calculate statistical summaries of student marks."""

    marks = np.array([
        [80, 70, 90],
        [60, 100, 75]
    ])

    print("\n=== Array Statistics ===")

    # Overall statistics
    print("Overall mean:", marks.mean())

    print(
        "Minimum / maximum:",
        marks.min(),
        marks.max()
    )

    # Column-wise average
    subject_means = marks.mean(axis=0)

    print(
        "Subject means (axis=0):",
        np.round(subject_means, 2)
    )

    # Row-wise average
    student_means = marks.mean(axis=1)

    print(
        "Student means (axis=1):",
        np.round(student_means, 2)
    )

    # Boolean filtering
    print(
        "Scores above 85:",
        marks[marks > 85]
    )

    # Limit values to a particular interval
    clipped_marks = np.clip(
        marks,
        65,
        90
    )

    print(
        "Clipped scores:\n",
        clipped_marks,
        sep=""
    )

    # Conditional operations
    performance_labels = np.where(
        marks >= 75,
        "Pass",
        "Review"
    )

    print(
        "Pass/review labels:\n",
        performance_labels,
        sep=""
    )


def demonstrate_normalization() -> None:
    """Standardize numerical readings using Z-scores."""

    readings = np.array([
        10, 20, 30, 40, 50
    ])

    standardized = z_score(readings)

    print("\n=== Z-Score Standardization ===")

    print(
        "Standardized readings:",
        np.round(standardized, 2)
    )

    # Check whether the mean is close to zero
    mean_is_zero = np.isclose(
        standardized.mean(),
        0
    )

    print(
        "Standardized mean is approximately zero:",
        mean_is_zero
    )

    # Handle an array with zero variance
    constant_values = np.array([5, 5, 5])

    print(
        "Constant input:",
        z_score(constant_values)
    )


def main() -> None:
    """Execute mathematical and statistical demonstrations."""

    demonstrate_arithmetic()
    demonstrate_statistics()
    demonstrate_normalization()


if __name__ == "__main__":
    main()