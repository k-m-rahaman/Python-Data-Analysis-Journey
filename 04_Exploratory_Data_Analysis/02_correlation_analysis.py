
"""
File: 02_correlation_analysis.py
Topic: Correlation Analysis

Description:
    Analyzes relationships between numerical variables
    using the Pandas correlation matrix.

Author: Kazi Mustafijur Rahaman
"""

import pandas as pd


def create_sales_data() -> pd.DataFrame:
    """Create a sample retail sales dataset."""

    data = {
        "order_id": list(range(1001, 1013)),

        "date": pd.date_range(
            start="2026-01-01",
            periods=12,
            freq="D"
        ),

        "city": [
            "Kolkata", "Durgapur", "Kolkata",
            "Siliguri", "Durgapur", "Kolkata",
            "Siliguri", "Kolkata", "Durgapur",
            "Siliguri", "Kolkata", "Durgapur"
        ],

        "category": [
            "Electronics", "Furniture", "Clothing",
            "Electronics", "Furniture", "Clothing",
            "Electronics", "Furniture", "Clothing",
            "Electronics", "Clothing", "Electronics"
        ],

        "product": [
            "Laptop", "Chair", "Shirt", "Phone",
            "Table", "Jeans", "Headphones", "Desk",
            "Jacket", "Monitor", "Shoes", "Keyboard"
        ],

        "units": [2, 1, 3, 1, 2, 4, 1, 2, 3, 1, 2, 5],

        "unit_price": [
            55000, 7000, 1200, 25000,
            8500, 1800, 3000, 9500,
            2200, 18000, 2500, 1500
        ],

        "discount_pct": [
            5, 10, 0, 8, 5, 0,
            10, 5, 0, 7, 5, 0
        ]
    }

    df = pd.DataFrame(data)

    df["revenue"] = (
        df["units"]
        * df["unit_price"]
        * (1 - df["discount_pct"] / 100)
    ).round(2)

    return df


def analyze_correlation() -> None:
    """Calculate correlations between numerical columns."""

    df = create_sales_data()

    print("=" * 55)
    print("CORRELATION ANALYSIS")
    print("=" * 55)

    # Select meaningful numerical columns.
    # order_id is an identifier, so we exclude it.

    numerical_columns = [
        "units",
        "unit_price",
        "discount_pct",
        "revenue"
    ]

    correlation_matrix = df[
        numerical_columns
    ].corr().round(2)

    print("\nCORRELATION MATRIX")

    print(correlation_matrix.to_string())

    print("\nCORRELATION WITH REVENUE")

    revenue_correlation = (
        correlation_matrix["revenue"]
        .drop("revenue")
        .sort_values(ascending=False)
    )

    print(revenue_correlation.to_string())

    print("\nINTERPRETATION")

    print("Positive correlation: variables move together.")
    print("Negative correlation: variables move oppositely.")
    print("Correlation does not prove causation.")


if __name__ == "__main__":
    analyze_correlation()
