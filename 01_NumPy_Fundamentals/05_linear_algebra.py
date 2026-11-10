"""
File: 05_linear_algebra.py
Topic: NumPy Linear Algebra Fundamentals

Description:
    Demonstrates matrix multiplication, transposition,
    dot products, vector norms, determinants,
    matrix inversion, linear equation solving,
    eigenvalues, and least-squares regression.

Author: Kazi Mustafijur Rahaman
"""

import numpy as np


def demonstrate_matrix_operations() -> None:
    """Perform fundamental matrix and vector operations."""

    first = np.array([
        [1, 2],
        [3, 4]
    ])

    second = np.array([
        [2, 0],
        [1, 2]
    ])

    vector = np.array([3, 4])

    print("=== Matrix Operations ===")

    # Matrix multiplication
    matrix_product = first @ second

    print(
        "Matrix multiplication:\n",
        matrix_product,
        sep=""
    )

    # Matrix transpose
    print(
        "Transpose:\n",
        first.T,
        sep=""
    )

    # Dot product of vectors
    dot_product = np.dot(
        vector,
        np.array([2, 5])
    )

    print(
        "Dot product:",
        dot_product
    )

    # Euclidean vector norm
    vector_length = np.linalg.norm(vector)

    print(
        "Vector length:",
        vector_length
    )


def demonstrate_linear_system() -> None:
    """
    Solve a system of linear equations.

    Equations:
        2x + y = 11
        x + 3y = 13

    Matrix form:
        AX = B
    """

    coefficients = np.array([
        [2.0, 1.0],
        [1.0, 3.0]
    ])

    totals = np.array([
        11.0,
        13.0
    ])

    # Solve the system directly
    solution = np.linalg.solve(
        coefficients,
        totals
    )

    # Calculate determinant
    determinant = np.linalg.det(
        coefficients
    )

    # Calculate matrix inverse
    inverse = np.linalg.inv(
        coefficients
    )

    print("\n=== Solving Linear Equations ===")

    print(
        "Determinant:",
        round(determinant, 2)
    )

    print(
        "Inverse:\n",
        np.round(inverse, 2),
        sep=""
    )

    print(
        "Solution [x, y]:",
        solution
    )

    # Verify the calculated solution
    verified = np.allclose(
        coefficients @ solution,
        totals
    )

    print(
        "Verified solution:",
        verified
    )

    # Example of a singular matrix
    singular = np.array([
        [1.0, 2.0],
        [2.0, 4.0]
    ])

    try:
        np.linalg.solve(
            singular,
            np.array([3.0, 6.0])
        )

    except np.linalg.LinAlgError:
        print(
            "Singular matrix handled: no unique solution."
        )


def demonstrate_eigenvalues_and_regression() -> None:
    """Calculate eigenvalues and fit a simple linear trend."""

    # Symmetric matrix
    symmetric = np.array([
        [2.0, 1.0],
        [1.0, 2.0]
    ])

    print("\n=== Eigenvalues and Least Squares ===")

    # Eigenvalues of a symmetric matrix
    eigenvalues = np.linalg.eigvalsh(
        symmetric
    )

    print(
        "Symmetric eigenvalues:",
        eigenvalues
    )

    # Example: weekly sales data
    weeks = np.array([
        1.0, 2.0, 3.0, 4.0
    ])

    sales = np.array([
        3.0, 5.0, 7.0, 9.0
    ])

    # Prepare the design matrix
    # Model: sales = slope * week + intercept
    design_matrix = np.column_stack((
        weeks,
        np.ones_like(weeks)
    ))

    # Least-squares regression
    slope, intercept = np.linalg.lstsq(
        design_matrix,
        sales,
        rcond=None
    )[0]

    print(
        f"Fitted line: sales = "
        f"{slope:.1f} * week + {intercept:.1f}"
    )

    # Predict week 5
    predicted_sales = slope * 5 + intercept

    print(
        f"Predicted sales for week 5: "
        f"{predicted_sales:.1f}"
    )


def main() -> None:
    """Run all linear algebra demonstrations."""

    demonstrate_matrix_operations()
    demonstrate_linear_system()
    demonstrate_eigenvalues_and_regression()


if __name__ == "__main__":
    main()