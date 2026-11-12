"""
Topic: Filtering and Sorting Pandas DataFrames

Analyze sample order data with comparison, multiple conditions,
category membership, text filters, sorting, and top-N selection.
"""

import pandas as pd


def create_orders() -> pd.DataFrame:
    """Generate illustrative store transactions."""
    orders = pd.DataFrame(
        {
            "order_id": [101, 102, 103, 104, 105, 106],
            "category": [
                "Electronics",
                "Office",
                "Grocery",
                "Electronics",
                "Office",
                "Grocery",
            ],
            "region": [
                "East",
                "West",
                "East",
                "North",
                "East",
                "South",
            ],
            "quantity": [2, 5, 10, 1, 4, 8],
            "unit_price": [
                800.0,
                150.0,
                60.0,
                1500.0,
                200.0,
                50.0,
            ],
        }
    )

    # Add a calculated revenue column.
    orders["revenue"] = (
        orders["quantity"] * orders["unit_price"]
    )

    return orders


def demonstrate_filtering(orders: pd.DataFrame) -> None:
    """Apply numerical, categorical, and combined filters."""

    print("=== Full Order Data ===")
    print(orders.to_string(index=False))

    # Filter high-revenue orders.
    high_value = orders.loc[
        orders["revenue"] >= 1000,
        ["order_id", "region", "revenue"],
    ]

    print(
        "\nRevenue >= 1000:\n",
        high_value.to_string(index=False),
        sep="",
    )

    # Filter multiple conditions.
    east_mid_value = orders.loc[
        orders["region"].eq("East")
        & orders["revenue"].between(600, 1000),
        ["order_id", "category", "revenue"],
    ]

    print(
        "\nEast orders with revenue 600-1000:\n",
        east_mid_value.to_string(index=False),
        sep="",
    )

    # Filter specified product categories.
    selected_categories = orders.loc[
        orders["category"].isin([
            "Electronics",
            "Office",
        ])
    ]

    print(
        "\nElectronics/Office order count:",
        len(selected_categories),
    )

    # Case-insensitive text filtering.
    matching = orders.loc[
        orders["category"].str.contains(
            "office",
            case=False,
            na=False,
        )
    ]

    print(
        "Office orders:",
        matching["order_id"].tolist(),
    )


def demonstrate_sorting(orders: pd.DataFrame) -> None:
    """Sort transactions and extract highest-revenue records."""

    # Sort revenue descending and order IDs ascending.
    sorted_orders = orders.sort_values(
        by=["revenue", "order_id"],
        ascending=[False, True],
        kind="stable",
    )

    # Identify top three orders.
    top_three = orders.nlargest(
        3,
        columns="revenue",
    )

    # Filter using an expressive query.
    queried = orders.query(
        "region == 'East' and revenue >= 600"
    )

    print("\n=== Sorting and Ranking ===")

    print(
        "Sorted order IDs:",
        sorted_orders["order_id"].tolist(),
    )

    print(
        "Top 3 revenue orders:\n",
        top_three[
            ["order_id", "revenue"]
        ].to_string(index=False),
        sep="",
    )

    print(
        "Matching query order IDs:",
        queried["order_id"].tolist(),
    )


def main() -> None:
    """Run filtering and sorting examples."""
    orders = create_orders()
    demonstrate_filtering(orders)
    demonstrate_sorting(orders)


if __name__ == "__main__":
    main()