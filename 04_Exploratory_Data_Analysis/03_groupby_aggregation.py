
"""
File: 03_groupby_aggregation.py
Topic: GroupBy and Aggregation

Description:
    Groups retail sales records by product category
    and city to calculate total sales, orders,
    units sold, and average revenue.

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


def analyze_groupby() -> None:
    """Perform grouping and aggregation."""

    df = create_sales_data()

    print("=" * 55)
    print("GROUPBY AND AGGREGATION ANALYSIS")
    print("=" * 55)

    # Group sales by product category.

    category_summary = (
        df.groupby("category")
        .agg(
            orders=("order_id", "count"),
            units_sold=("units", "sum"),
            total_revenue=("revenue", "sum"),
            average_order_value=("revenue", "mean")
        )
        .sort_values(
            by="total_revenue",
            ascending=False
        )
        .round(2)
    )

    print("\nCATEGORY PERFORMANCE")

    print(
        category_summary.to_string(
            float_format=lambda value: f"{value:,.2f}"
        )
    )

    # Group sales by city.

    city_summary = (
        df.groupby("city")
        .agg(
            orders=("order_id", "count"),
            units_sold=("units", "sum"),
            total_revenue=("revenue", "sum")
        )
        .sort_values(
            by="total_revenue",
            ascending=False
        )
        .round(2)
    )

    print("\nCITY PERFORMANCE")

    print(
        city_summary.to_string(
            float_format=lambda value: f"{value:,.2f}"
        )
    )


if __name__ == "__main__":
    analyze_groupby()
