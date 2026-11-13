"""
File: 02_duplicates.py
Topic: Duplicate Detection and Removal

Demonstrates exact duplicate detection, duplicate business keys,
and safe removal of repeated records.
"""

import pandas as pd


def create_dataset() -> pd.DataFrame:
    """Create employee records containing duplicates."""

    return pd.DataFrame({
        "employee_id": [101, 102, 103, 103, 104],
        "name": ["Asha", "Ravi", "Mira", "Mira", "Asha"],
        "email": [
            "asha@example.com",
            "ravi@example.com",
            "mira@example.com",
            "mira@example.com",
            "asha@example.com"
        ],
        "city": ["Kolkata", "Durgapur", "Suri", "Suri", "Kolkata"]
    })


def detect_duplicates(df: pd.DataFrame) -> None:
    """Find exact duplicate records."""

    print("=== Original Dataset ===")
    print(df.to_string(index=False))

    print("\nExact duplicate count:", df.duplicated().sum())

    duplicates = df[df.duplicated(keep=False)]

    print("\n=== Exact Duplicate Records ===")
    print(duplicates.to_string(index=False))


def remove_exact_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Remove completely identical rows."""

    cleaned = df.drop_duplicates()

    print("\n=== After Removing Exact Duplicates ===")
    print(cleaned.to_string(index=False))

    return cleaned


def remove_duplicate_emails(df: pd.DataFrame) -> pd.DataFrame:
    """Remove records with repeated email addresses."""

    duplicate_emails = df[
        df.duplicated(subset=["email"], keep=False)
    ]

    print("\n=== Duplicate Email Records ===")
    print(duplicate_emails.to_string(index=False))

    cleaned = df.drop_duplicates(
        subset=["email"],
        keep="first"
    )

    print("\n=== Final Unique Employees ===")
    print(cleaned.to_string(index=False))

    return cleaned


def main() -> None:
    """Execute duplicate-cleaning demonstrations."""

    df = create_dataset()

    detect_duplicates(df)

    exact_cleaned = remove_exact_duplicates(df)

    final_cleaned = remove_duplicate_emails(exact_cleaned)

    print("\nOriginal rows:", len(df))
    print("Final unique employees:", len(final_cleaned))


if __name__ == "__main__":
    main()