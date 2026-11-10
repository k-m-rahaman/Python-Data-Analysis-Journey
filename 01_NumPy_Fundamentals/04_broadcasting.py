"""
File: 04_broadcasting.py
Topic: NumPy Broadcasting

Description:
    Demonstrates broadcasting rules, shape
    compatibility, row-column operations,
    practical sales calculations, and
    feature centering.

Author: Kazi Mustafijur Rahaman
"""

import numpy as np


def demonstrate_basic_broadcasting() -> None:
    """Perform operations on arrays with compatible shapes."""

    # Shape: (3, 1)
    row_adjustments = np.array([
        1, 2, 3
    ])[:, np.newaxis]

    # Shape: (4,)
    column_values = np.array([
        10, 20, 30, 40
    ])

    print("=== Broadcasting Shape Rules ===")

    print(
        "Column shape:",
        row_adjustments.shape
    )

    print(
        "Row shape:",
        column_values.shape
    )

    result_shape = np.broadcast_shapes(
        row_adjustments.shape,
        column_values.shape
    )

    print(
        "Result shape:",
        result_shape
    )

    # Broadcasting produces a 3x4 result
    result = row_adjustments + column_values

    print(
        "Broadcast sum:\n",
        result,
        sep=""
    )


def demonstrate_store_revenue() -> None:
    """Calculate revenue and apply different store discounts."""

    # Three stores and four products
    quantities = np.array([
        [2, 1, 5, 0],
        [1, 3, 2, 4],
        [0, 2, 4, 3]
    ])

    # Price of each product
    unit_prices = np.array([
        120.0,
        250.0,
        80.0,
        150.0
    ])

    # Different discount rates for each store
    discount_rates = np.array([
        [0.05],
        [0.10],
        [0.00]
    ])

    # Input validation
    if quantities.shape[1] != unit_prices.size:
        raise ValueError(
            "Each product must have one unit price."
        )

    if discount_rates.shape != (
        quantities.shape[0], 1
    ):
        raise ValueError(
            "Each store must have one discount rate."
        )

    # Broadcasting price across every store
    item_revenue = quantities * unit_prices

    # Total gross revenue for each store
    gross_revenue = item_revenue.sum(axis=1)

    # Apply store-specific discounts
    discounted_revenue = item_revenue * (
        1 - discount_rates
    )

    # Total revenue after discounts
    net_revenue = discounted_revenue.sum(axis=1)

    print("\n=== Practical Store Revenue Analysis ===")

    print(
        "Item revenue:\n",
        item_revenue,
        sep=""
    )

    print(
        "Gross revenue by store:",
        gross_revenue
    )

    print(
        "Discounted revenue by store:",
        np.round(net_revenue, 2)
    )


def demonstrate_column_centering() -> None:
    """Center each feature around its column average."""

    measurements = np.array([
        [20.0, 30.0, 40.0],
        [25.0, 35.0, 45.0]
    ])

    # Column means have shape (3,)
    column_means = measurements.mean(axis=0)

    # Subtract the means using broadcasting
    centered = measurements - column_means

    print("\n=== Feature Centering ===")

    print(
        "Column averages:",
        column_means
    )

    print(
        "Centered features:\n",
        centered,
        sep=""
    )

    # Demonstrate incompatible shapes
    try:
        np.broadcast_shapes(
            (3, 4),
            (2, 3)
        )

    except ValueError:
        print(
            "Incompatible shapes (3, 4) and "
            "(2, 3) safely detected."
        )


def main() -> None:
    """Execute all broadcasting demonstrations."""

    demonstrate_basic_broadcasting()
    demonstrate_store_revenue()
    demonstrate_column_centering()


if __name__ == "__main__":
    main()