
"""
File: 04_pivot_tables_crosstab.py
Topic: Pivot Tables and Crosstab

Description:
    Creates pivot tables and cross-tabulations
    to compare retail revenue across cities
    and product categories.

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


def analyze_pivot_tables() -> None:
    """Generate pivot tables and cross-tabulations."""

    df = create_sales_data()

    print("=" * 55)
    print("PIVOT TABLE AND CROSSTAB ANALYSIS")
    print("=" * 55)

    # Pivot table: Revenue by category and city.

    revenue_pivot = pd.pivot_table(
        df,
        values="revenue",
        index="category",
        columns="city",
        aggfunc="sum",
        fill_value=0,
        margins=True,
        margins_name="All"
    )

    print("\nREVENUE BY CATEGORY AND CITY")

    print(
        revenue_pivot.to_string(
            float_format=lambda value: f"{value:,.2f}"
        )
    )

    # Crosstab: Count orders by category and city.

    category_city_count = pd.crosstab(
        df["category"],
        df["city"],
        margins=True,
        margins_name="All"
    )

    print("\nORDER COUNT BY CATEGORY AND CITY")

    print(category_city_count.to_string())


if __name__ == "__main__":
    analyze_pivot_tables()
