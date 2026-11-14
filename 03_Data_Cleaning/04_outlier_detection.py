"""
File: 04_outlier_detection.py
Topic: Outlier Detection Using IQR

Demonstrates quartiles, interquartile range,
outlier identification, and value capping.
"""

import pandas as pd


def create_dataset() -> pd.DataFrame:
    """Create a sample delivery-time dataset."""

    return pd.DataFrame({
        "delivery_id": range(101, 110),
        "delivery_days": [20, 22, 23, 24, 25, 26, 27, 28, 100]
    })


def calculate_iqr(df: pd.DataFrame) -> tuple[float, float]:
    """Calculate lower and upper IQR boundaries."""

    q1 = df["delivery_days"].quantile(0.25)

    q3 = df["delivery_days"].quantile(0.75)

    iqr = q3 - q1

    lower_bound = q1 - (1.5 * iqr)

    upper_bound = q3 + (1.5 * iqr)

    print("=== IQR Statistics ===")
    print("Q1:", q1)
    print("Q3:", q3)
    print("IQR:", iqr)
    print("Lower bound:", lower_bound)
    print("Upper bound:", upper_bound)

    return lower_bound, upper_bound


def detect_outliers(
    df: pd.DataFrame,
    lower: float,
    upper: float
) -> pd.DataFrame:
    """Find values outside the IQR boundaries."""

    mask = (
        (df["delivery_days"] < lower)
        | (df["delivery_days"] > upper)
    )

    outliers = df.loc[mask]

    print("\n=== Detected Outliers ===")
    print(outliers.to_string(index=False))

    print("\nOutlier count:", len(outliers))

    return outliers


def cap_outliers(
    df: pd.DataFrame,
    lower: float,
    upper: float
) -> pd.DataFrame:
    """Create a capped version of the delivery data."""

    cleaned = df.copy()

    cleaned["capped_delivery_days"] = (
        cleaned["delivery_days"].clip(
            lower=lower,
            upper=upper
        )
    )

    print("\n=== Dataset After Capping ===")
    print(cleaned.to_string(index=False))

    return cleaned


def main() -> None:
    """Execute IQR-based outlier detection."""

    df = create_dataset()

    print("=== Original Dataset ===")
    print(df.to_string(index=False))

    lower, upper = calculate_iqr(df)

    detect_outliers(df, lower, upper)

    cap_outliers(df, lower, upper)


if __name__ == "__main__":
    main()