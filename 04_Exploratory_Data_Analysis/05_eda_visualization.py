
"""
File: 05_eda_visualization.py
Topic: EDA Visualization

Description:
    Visualizes retail sales data using Matplotlib
    and Seaborn.

    Generates:
    1. Revenue by category bar chart.
    2. Revenue distribution histogram.
    3. Units versus revenue scatter plot.

Author: Kazi Mustafijur Rahaman
"""

from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


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


def visualize_sales_data() -> None:
    """Generate and save EDA visualizations."""

    df = create_sales_data()

    sns.set_theme(style="whitegrid")

    # Create output directory.

    output_dir = Path(__file__).resolve().parent / "outputs"

    output_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    print("=" * 55)
    print("EXPLORATORY DATA ANALYSIS VISUALIZATION")
    print("=" * 55)

    print(f"\nTotal orders: {len(df)}")

    print(
        f"Total revenue: INR "
        f"{df['revenue'].sum():,.2f}"
    )

    # --------------------------------------------------
    # 1. BAR CHART: Revenue by Category
    # --------------------------------------------------

    category_revenue = (
        df.groupby("category", as_index=False)["revenue"]
        .sum()
        .sort_values("revenue", ascending=False)
    )

    fig, ax = plt.subplots(figsize=(9, 5))

    sns.barplot(
        data=category_revenue,
        x="category",
        y="revenue",
        color="steelblue",
        ax=ax
    )

    ax.set_title("Revenue by Product Category")
    ax.set_xlabel("Product Category")
    ax.set_ylabel("Revenue (INR)")

    fig.tight_layout()

    fig.savefig(
        output_dir / "01_revenue_by_category.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()
    plt.close(fig)

    # --------------------------------------------------
    # 2. HISTOGRAM: Revenue Distribution
    # --------------------------------------------------

    fig, ax = plt.subplots(figsize=(9, 5))

    sns.histplot(
        data=df,
        x="revenue",
        bins=6,
        kde=True,
        color="darkorange",
        ax=ax
    )

    ax.set_title("Revenue Distribution")
    ax.set_xlabel("Revenue (INR)")
    ax.set_ylabel("Number of Orders")

    fig.tight_layout()

    fig.savefig(
        output_dir / "02_revenue_distribution.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()
    plt.close(fig)

    # --------------------------------------------------
    # 3. SCATTER PLOT: Units vs Revenue
    # --------------------------------------------------

    fig, ax = plt.subplots(figsize=(9, 5))

    sns.scatterplot(
        data=df,
        x="units",
        y="revenue",
        hue="category",
        s=100,
        ax=ax
    )

    ax.set_title("Units Sold vs Revenue")
    ax.set_xlabel("Units Sold")
    ax.set_ylabel("Revenue (INR)")

    fig.tight_layout()

    fig.savefig(
        output_dir / "03_units_vs_revenue.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()
    plt.close(fig)

    print("\nAll visualizations generated successfully!")

    print("\nSaved chart files:")

    print("1. 01_revenue_by_category.png")
    print("2. 02_revenue_distribution.png")
    print("3. 03_units_vs_revenue.png")

    print("\nOutput directory: outputs/")


if __name__ == "__main__":
    visualize_sales_data()
