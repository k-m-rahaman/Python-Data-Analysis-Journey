
"""
File: 01_feature_engineering_fundamentals.py
Topic: Feature Engineering Fundamentals

Description:
Creates meaningful new features from existing customer data.

Author: Kazi Mustafijur Rahaman
"""

import pandas as pd


def create_customer_data() -> pd.DataFrame:
    """Create a sample customer dataset."""

    return pd.DataFrame({
        "customer_id": [101, 102, 103, 104, 105],
        "age": [22, 31, 45, 28, 52],
        "monthly_income": [25000, 42000, 65000, 35000, 72000],
        "orders_count": [2, 5, 8, 3, 10],
        "total_spent": [3000, 12500, 28000, 5400, 45000],
        "membership": [
            "Basic", "Premium", "Premium", "Basic", "Premium"
        ],
        "signup_date": pd.to_datetime([
            "2025-01-15",
            "2025-06-10",
            "2024-12-01",
            "2025-09-20",
            "2025-03-05"
        ])
    })


def engineer_features(data: pd.DataFrame) -> pd.DataFrame:
    """Generate useful features from existing columns."""

    df = data.copy()

    # Average spending per order
    df["average_order_value"] = (
        df["total_spent"] / df["orders_count"]
    ).round(2)

    # Customer age categories
    df["age_group"] = pd.cut(
        df["age"],
        bins=[0, 25, 40, 60, 100],
        labels=["Young", "Adult", "Mature", "Senior"],
        include_lowest=True
    )

    # Customer membership as numerical data
    df["is_premium"] = (
        df["membership"] == "Premium"
    ).astype(int)

    # Customer tenure in days
    reference_date = pd.Timestamp("2026-11-21")

    df["tenure_days"] = (
        reference_date - df["signup_date"]
    ).dt.days

    # Extract signup month
    df["signup_month"] = df["signup_date"].dt.month

    # Spending compared with monthly income
    df["spend_income_ratio"] = (
        df["total_spent"] / df["monthly_income"]
    ).round(3)

    return df


def main():
    print("=" * 55)
    print("FEATURE ENGINEERING FUNDAMENTALS")
    print("=" * 55)

    customers = create_customer_data()

    print("\nOriginal Dataset:")
    print(customers.head().to_string(index=False))

    engineered_data = engineer_features(customers)

    print("\nEngineered Features:")
    print(
        engineered_data[
            [
                "customer_id",
                "age_group",
                "average_order_value",
                "is_premium",
                "tenure_days",
                "signup_month"
            ]
        ].to_string(index=False)
    )


if __name__ == "__main__":
    main()
