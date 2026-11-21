
"""
File: 02_feature_scaling.py
Topic: Feature Scaling and Normalization

Description:
Demonstrates standardization, normalization,
and robust scaling using Scikit-learn.

Author: Kazi Mustafijur Rahaman
"""

import pandas as pd

from sklearn.preprocessing import (
    StandardScaler,
    MinMaxScaler,
    RobustScaler
)


def create_dataset() -> pd.DataFrame:
    """Create a sample dataset."""

    return pd.DataFrame({
        "age": [20, 25, 30, 35, 40],
        "annual_income": [20000, 30000, 40000, 50000, 60000],
        "purchase_count": [1, 2, 3, 4, 5]
    })


def demonstrate_scaling(data: pd.DataFrame):
    """Apply different scaling techniques."""

    scalers = {
        "StandardScaler": StandardScaler(),
        "MinMaxScaler": MinMaxScaler(),
        "RobustScaler": RobustScaler()
    }

    for name, scaler in scalers.items():

        scaled_values = scaler.fit_transform(data)

        scaled_data = pd.DataFrame(
            scaled_values,
            columns=data.columns
        )

        print(f"\n{name}")
        print("-" * 40)

        print(scaled_data.round(2).to_string(index=False))


def main():
    print("=" * 55)
    print("FEATURE SCALING AND NORMALIZATION")
    print("=" * 55)

    data = create_dataset()

    print("\nOriginal Dataset:")
    print(data.to_string(index=False))

    demonstrate_scaling(data)


if __name__ == "__main__":
    main()
