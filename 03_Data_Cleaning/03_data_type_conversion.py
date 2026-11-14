"""
File: 03_data_type_conversion.py
Topic: Data Type Conversion

Demonstrates numeric conversion, date parsing,
string standardization, and invalid-value handling.
"""

import pandas as pd


def create_dataset() -> pd.DataFrame:
    """Create a dataset containing inconsistent data types."""

    return pd.DataFrame({
        "invoice_id": ["INV001", "INV002", "INV003", "INV004"],
        "amount": ["₹1,200.50", "850", "invalid", "2,000"],
        "order_date": [
            "2026-10-01",
            "2026-10-02",
            "not-a-date",
            "2026-10-04"
        ],
        "status": [" PAID ", "pending", "PAID", " cancelled "]
    })


def convert_data_types(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and convert columns into appropriate types."""

    cleaned = df.copy()

    # Remove currency symbols and commas.
    cleaned["amount"] = (
        cleaned["amount"]
        .astype("string")
        .str.replace(r"[₹,]", "", regex=True)
    )

    # Convert amount into numeric values.
    cleaned["amount"] = pd.to_numeric(
        cleaned["amount"],
        errors="coerce"
    )

    # Convert dates into datetime objects.
    cleaned["order_date"] = pd.to_datetime(
        cleaned["order_date"],
        errors="coerce"
    )

    # Standardize text.
    cleaned["status"] = (
        cleaned["status"]
        .astype("string")
        .str.strip()
        .str.lower()
    )

    # Convert repeated categories into category dtype.
    cleaned["status"] = cleaned["status"].astype("category")

    return cleaned


def display_results(df: pd.DataFrame) -> None:
    """Display cleaned data and resulting data types."""

    print("=== Cleaned Dataset ===")
    print(df.to_string(index=False))

    print("\n=== Data Types ===")
    print(df.dtypes.to_string())

    print("\nInvalid numeric values:", df["amount"].isna().sum())

    print("Invalid dates:", df["order_date"].isna().sum())

    print(
        "\nTotal valid invoice amount:",
        df["amount"].sum()
    )


def main() -> None:
    """Execute data type conversion."""

    original = create_dataset()

    print("=== Original Data Types ===")
    print(original.dtypes.to_string())

    cleaned = convert_data_types(original)

    display_results(cleaned)


if __name__ == "__main__":
    main()