
"""
File: 01_descriptive_statistics.py
Topic: Descriptive Statistics

Description:
    Analyzes retail sales data using statistical measures
    such as mean, median, standard deviation, minimum,
    maximum, and quartiles.

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


def analyze_descriptive_statistics() -> None:
    """Calculate and display descriptive statistics."""

    df = create_sales_data()

    print("=" * 55)
    print("DESCRIPTIVE STATISTICS ANALYSIS")
    print("=" * 55)

    print("\nDATASET OVERVIEW")

    print(f"Total rows: {len(df)}")
    print(f"Total columns: {df.shape[1]}")

    print(f"Total revenue: INR {df['revenue'].sum():,.2f}")

    print(
        f"Average revenue: INR "
        f"{df['revenue'].mean():,.2f}"
    )

    print(
        f"Median revenue: INR "
        f"{df['revenue'].median():,.2f}"
    )

    print(
        f"Highest revenue: INR "
        f"{df['revenue'].max():,.2f}"
    )

    print(
        f"Lowest revenue: INR "
        f"{df['revenue'].min():,.2f}"
    )

    print("\nNUMERICAL SUMMARY")

    numerical_summary = df[
        ["units", "unit_price", "discount_pct", "revenue"]
    ].describe().round(2)

    print(numerical_summary.to_string())


if __name__ == "__main__":
    analyze_descriptive_statistics()
