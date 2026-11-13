"""
File: 01_missing_values.py
Topic: Handling Missing Values

Demonstrates missing-value detection, statistical imputation,
and removal of incomplete records.
"""

import pandas as pd


def create_dataset() -> pd.DataFrame:
    """Create a sample employee dataset with missing values."""

    return pd.DataFrame({
        "employee_id": ["E001", "E002", "E003", "E004", "E005"],
        "name": ["Asha", "Ravi", "Mira", "Neha", "Kabir"],
        "age": [24, None, 29, None, 35],
        "salary": [35000, 42000, None, 50000, None],
        "department": ["IT", "HR", None, "IT", "Finance"]
    })


def inspect_missing_values(df: pd.DataFrame) -> None:
    """Identify missing values in each column."""

    print("=== Original Dataset ===")
    print(df.to_string(index=False))

    print("\n=== Missing Values Count ===")
    print(df.isnull().sum().to_string())

    print("\nTotal missing values:", df.isnull().sum().sum())


def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """Replace missing values using statistical methods."""

    cleaned = df.copy()

    # Fill numerical columns using median.
    cleaned["age"] = cleaned["age"].fillna(
        cleaned["age"].median()
    )

    cleaned["salary"] = cleaned["salary"].fillna(
        cleaned["salary"].median()
    )

    # Fill categorical values using mode.
    cleaned["department"] = cleaned["department"].fillna(
        cleaned["department"].mode().iloc[0]
    )

    return cleaned


def demonstrate_dropna(df: pd.DataFrame) -> None:
    """Demonstrate removing incomplete rows."""

    dropped = df.dropna()

    print("\n=== Dataset After dropna() ===")
    print(dropped.to_string(index=False))

    print("Rows remaining:", len(dropped))


def main() -> None:
    """Execute missing-value demonstrations."""

    df = create_dataset()

    inspect_missing_values(df)

    cleaned = handle_missing_values(df)

    print("\n=== Cleaned Dataset ===")
    print(cleaned.to_string(index=False))

    print("\nRemaining missing values:")
    print(cleaned.isnull().sum().to_string())

    demonstrate_dropna(df)


if __name__ == "__main__":
    main()