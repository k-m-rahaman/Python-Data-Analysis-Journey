
"""
File: 03_sampling_techniques.py
Topic: Sampling Techniques

Description:
    Demonstrates different sampling techniques
    using an employee salary dataset.

Author: Kazi Mustafijur Rahaman
"""

import pandas as pd


def create_population():
    """Create an employee population dataset."""

    return pd.DataFrame({
        "employee_id": [
            f"E{i:02d}" for i in range(1, 13)
        ],

        "department": (
            ["IT"] * 4
            + ["Sales"] * 4
            + ["HR"] * 4
        ),

        "salary": [
            45000, 48000, 52000, 55000,
            30000, 32000, 35000, 38000,
            40000, 42000, 44000, 46000
        ]
    })


def display_sample(title, sample):
    """Display a sample and its average salary."""

    print(f"\n{title}")

    print(
        sample[
            ["employee_id", "department", "salary"]
        ].to_string(index=False)
    )

    print(
        f"Sample mean salary: "
        f"{sample['salary'].mean():,.2f}"
    )


def analyze_sampling():
    """Demonstrate different sampling methods."""

    df = create_population()

    print("=" * 55)
    print("SAMPLING TECHNIQUES")
    print("=" * 55)

    print("\nPOPULATION INFORMATION")

    print(f"Total employees: {len(df)}")

    print(
        f"Population mean salary: "
        f"{df['salary'].mean():,.2f}"
    )

    # 1. Simple Random Sampling

    random_sample = (
        df.sample(n=4, random_state=42)
        .sort_values("employee_id")
    )

    display_sample(
        "1. SIMPLE RANDOM SAMPLING",
        random_sample
    )

    # 2. Systematic Sampling
    # Select every third employee.

    systematic_sample = df.iloc[::3]

    display_sample(
        "2. SYSTEMATIC SAMPLING",
        systematic_sample
    )

    # 3. Stratified Sampling
    # Select two employees from each department.

    stratified_sample = (
        df.groupby(
            "department",
            group_keys=False
        )
        .sample(n=2, random_state=42)
        .sort_values(
            ["department", "employee_id"]
        )
    )

    display_sample(
        "3. STRATIFIED SAMPLING",
        stratified_sample
    )


if __name__ == "__main__":
    analyze_sampling()
