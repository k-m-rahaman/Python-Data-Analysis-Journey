"""
Topic: Pandas Series Fundamentals

Learn labeled one-dimensional data, selection, missing values,
vectorized operations, and automatic index alignment.
"""

import pandas as pd


def demonstrate_series() -> None:
    """Create a labeled Series and inspect its main properties."""
    marks = pd.Series(
        [78, 85, 92, 74],
        index=["Asha", "Rahul", "Mira", "Kabir"],
        name="exam_marks",
        dtype="int64",
    )

    print("=== Series Basics ===")
    print(marks.to_string())
    print("Length:", len(marks))
    print("Data type:", marks.dtype)
    print("Average marks:", marks.mean())
    print("Highest marks:", marks.max())
    print("Rahul's marks (loc):", marks.loc["Rahul"])
    print("First student's marks (iloc):", marks.iloc[0])
    print("Marks >= 80:\n", marks[marks >= 80].to_string(), sep="")

    # Different order: pandas matches labels, not positions.
    bonus = pd.Series({"Mira": 3, "Kabir": 4, "Asha": 5, "Rahul": 2})
    adjusted = (marks + bonus).clip(upper=100)
    print("Adjusted marks:\n", adjusted.to_string(), sep="")


def demonstrate_missing_values() -> None:
    """Recognize missing scores and replace them using a median."""
    scores = pd.Series(
        [82, None, 75, 91],
        index=["S001", "S002", "S003", "S004"],
        name="quiz_scores",
        dtype="Float64",
    )
    filled_scores = scores.fillna(scores.median())

    print("\n=== Missing Values ===")
    print("Missing count:", scores.isna().sum())
    print("Median:", scores.median())
    print("Filled scores:\n", filled_scores.to_string(), sep="")


def main() -> None:
    """Run Pandas Series examples."""
    demonstrate_series()
    demonstrate_missing_values()


if __name__ == "__main__":
    main()