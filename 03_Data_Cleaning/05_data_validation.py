"""
File: 05_data_validation.py
Topic: Data Validation and Cleaning Pipeline

Demonstrates required-column checks, email validation,
numeric validation, duplicate removal, and clean data output.
"""

import pandas as pd


REQUIRED_COLUMNS = {
    "order_id",
    "customer",
    "email",
    "quantity",
    "unit_price"
}

EMAIL_PATTERN = r"[^@\s]+@[^@\s]+\.[^@\s]+"


def create_dataset() -> pd.DataFrame:
    """Create sample order records with data-quality issues."""

    return pd.DataFrame({
        "order_id": [
            "O101", "O102", "O103",
            "O104", "O105", "O105"
        ],
        "customer": [
            "Asha", "Ravi", None,
            "Mira", "Kabir", "Kabir"
        ],
        "email": [
            "asha@example.com",
            "bad-email",
            "mira@example.com",
            "mira@example.com",
            "kabir@example.com",
            "kabir@example.com"
        ],
        "quantity": [2, 1, 2, -1, 3, 3],
        "unit_price": [100, 200, 50, 150, 80, 80]
    })


def validate_columns(df: pd.DataFrame) -> None:
    """Check whether all required columns are available."""

    missing = REQUIRED_COLUMNS - set(df.columns)

    if missing:
        raise ValueError(
            f"Missing required columns: {sorted(missing)}"
        )


def clean_orders(
    df: pd.DataFrame
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Validate records and separate clean, rejected, and duplicate data."""

    validate_columns(df)

    cleaned = df.copy()

    # Standardize text columns.
    for column in ["order_id", "customer", "email"]:
        cleaned[column] = (
            cleaned[column]
            .astype("string")
            .str.strip()
            .replace("", pd.NA)
        )

    # Convert numerical columns safely.
    cleaned["quantity"] = pd.to_numeric(
        cleaned["quantity"],
        errors="coerce"
    )

    cleaned["unit_price"] = pd.to_numeric(
        cleaned["unit_price"],
        errors="coerce"
    )

    # Validate emails.
    valid_email = cleaned["email"].str.fullmatch(
        EMAIL_PATTERN,
        na=False
    )

    # Apply all validation conditions.
    valid_mask = (
        cleaned[["order_id", "customer", "email"]]
        .notna()
        .all(axis=1)
        & valid_email
        & cleaned["quantity"].gt(0)
        & cleaned["unit_price"].ge(0)
    )

    # Keep invalid records separately for investigation.
    rejected = cleaned.loc[~valid_mask].copy()

    valid = cleaned.loc[valid_mask].copy()

    # Detect duplicate order IDs.
    duplicate_mask = valid.duplicated(
        subset=["order_id"],
        keep="first"
    )

    duplicates = valid.loc[duplicate_mask].copy()

    # Remove duplicate order IDs.
    final_cleaned = valid.drop_duplicates(
        subset=["order_id"],
        keep="first"
    ).copy()

    # Calculate transaction totals.
    final_cleaned["total_amount"] = (
        final_cleaned["quantity"]
        * final_cleaned["unit_price"]
    )

    return final_cleaned, rejected, duplicates


def main() -> None:
    """Execute the complete data-cleaning pipeline."""

    df = create_dataset()

    print("=== Original Records ===")
    print(df.to_string(index=False))

    cleaned, rejected, duplicates = clean_orders(df)

    print("\n=== Clean Records ===")
    print(cleaned.to_string(index=False))

    print("\n=== Rejected Records ===")
    print(rejected.to_string(index=False))

    print("\n=== Duplicate Records Removed ===")
    print(duplicates.to_string(index=False))

    print("\n=== Cleaning Summary ===")
    print("Original records:", len(df))
    print("Clean records:", len(cleaned))
    print("Rejected records:", len(rejected))
    print("Duplicate records removed:", len(duplicates))

    print(
        "Total revenue:",
        cleaned["total_amount"].sum()
    )


if __name__ == "__main__":
    main()