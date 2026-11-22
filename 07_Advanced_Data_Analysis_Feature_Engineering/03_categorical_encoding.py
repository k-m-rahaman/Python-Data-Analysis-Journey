
"""
File: 03_categorical_encoding.py
Topic: Encoding Categorical Variables

Description:
Converts categorical data into numerical features
using One-Hot and Ordinal Encoding.

Author: Kazi Mustafijur Rahaman
"""

import pandas as pd


def create_employee_data() -> pd.DataFrame:
    """Create sample employee records."""

    return pd.DataFrame({
        "employee_id": [101, 102, 103, 104, 105],
        "department": [
            "Sales", "IT", "HR", "IT", "Sales"
        ],
        "experience_level": [
            "Junior", "Mid", "Senior", "Junior", "Senior"
        ],
        "remote": [
            "Yes", "No", "Yes", "No", "Yes"
        ]
    })


def encode_categories(data: pd.DataFrame) -> pd.DataFrame:
    """Encode categorical columns."""

    df = data.copy()

    # One-Hot Encoding
    department_encoded = pd.get_dummies(
        df["department"],
        prefix="department",
        dtype=int
    )

    # Ordinal Encoding
    experience_mapping = {
        "Junior": 1,
        "Mid": 2,
        "Senior": 3
    }

    experience_encoded = (
        df["experience_level"]
        .map(experience_mapping)
        .rename("experience_encoded")
    )

    # Binary Encoding
    remote_encoded = (
        df["remote"]
        .map({"No": 0, "Yes": 1})
        .rename("remote_encoded")
    )

    # Combine encoded features
    encoded_data = pd.concat(
        [
            df[["employee_id"]],
            department_encoded,
            experience_encoded,
            remote_encoded
        ],
        axis=1
    )

    return encoded_data


def main():
    print("=" * 55)
    print("CATEGORICAL ENCODING")
    print("=" * 55)

    employees = create_employee_data()

    print("\nOriginal Dataset:")
    print(employees.to_string(index=False))

    encoded = encode_categories(employees)

    print("\nEncoded Dataset:")
    print(encoded.to_string(index=False))


if __name__ == "__main__":
    main()
