
"""
File: 04_outlier_detection.py
Topic: Outlier Detection and Treatment

Description:
Detects unusual salary values using IQR
and demonstrates outlier capping.

Author: Kazi Mustafijur Rahaman
"""

import pandas as pd


def create_salary_data() -> pd.DataFrame:
    """Create employee salary dataset."""

    return pd.DataFrame({
        "employee_id": [
            101, 102, 103, 104,
            105, 106, 107, 108
        ],
        "salary": [
            32000, 35000, 36000, 37000,
            38000, 39000, 40000, 150000
        ]
    })


def calculate_iqr_bounds(series: pd.Series):
    """Calculate lower and upper IQR boundaries."""

    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)

    iqr = q3 - q1

    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    return q1, q3, iqr, lower_bound, upper_bound


def detect_outliers(data: pd.DataFrame, column: str):
    """Identify outliers using IQR."""

    q1, q3, iqr, lower, upper = calculate_iqr_bounds(
        data[column]
    )

    outliers = data[
        (data[column] < lower) |
        (data[column] > upper)
    ]

    return outliers, lower, upper, iqr


def cap_outliers(data: pd.DataFrame, column: str):
    """Replace extreme values with IQR boundaries."""

    _, lower, upper, _ = detect_outliers(data, column)

    result = data.copy()

    result[column] = result[column].clip(
        lower=lower,
        upper=upper
    )

    return result


def main():
    print("=" * 55)
    print("OUTLIER DETECTION AND TREATMENT")
    print("=" * 55)

    data = create_salary_data()

    print("\nOriginal Salary Data:")
    print(data.to_string(index=False))

    outliers, lower, upper, iqr = detect_outliers(
        data, "salary"
    )

    print("\nIQR Analysis:")
    print(f"IQR: {iqr:.2f}")
    print(f"Lower Bound: {lower:.2f}")
    print(f"Upper Bound: {upper:.2f}")

    print("\nDetected Outliers:")
    print(outliers.to_string(index=False))

    cleaned_data = cap_outliers(data, "salary")

    print("\nSalary Data After Capping:")
    print(cleaned_data.to_string(index=False))


if __name__ == "__main__":
    main()
