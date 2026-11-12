"""
Topic: Pandas DataFrame Indexing

Demonstrate label-based and positional selection, scalar access,
index updates, reindexing, index alignment, and MultiIndex.
"""

import pandas as pd


def create_student_data() -> pd.DataFrame:
    """Create a student table with unique student IDs."""
    students = pd.DataFrame(
        {
            "student_id": [
                "S001", "S002", "S003", "S004", "S005"
            ],
            "name": [
                "Asha", "Ravi", "Mira", "Neha", "Kabir"
            ],
            "course": [
                "Python", "SQL", "Python", "SQL", "Python"
            ],
            "score": [82, 77, 86, 91, 74],
            "attendance": [95, 88, 92, 90, 80],
        }
    )

    # Ensure that IDs are unique.
    if students["student_id"].duplicated().any():
        raise ValueError("Student IDs must be unique.")

    # Use student ID as the index.
    return students.set_index("student_id")


def demonstrate_selection(students: pd.DataFrame) -> None:
    """Compare loc, iloc, at and iat."""

    print("=== Index Selection ===")

    print(
        "Index name:",
        students.index.name
    )

    # Label-based selection.
    print(
        "S002 student:",
        students.loc["S002", "name"]
    )

    # Position-based selection.
    print(
        "First student (iloc):",
        students.iloc[0]["name"]
    )

    # Efficient scalar access by label.
    print(
        "S003 score (at):",
        students.at["S003", "score"]
    )

    # Efficient scalar access by position.
    print(
        "Second student's score (iat):",
        students.iat[1, 2]
    )

    # Label-based slicing: end label included.
    print(
        "\nLabel slice S002:S004 (end included):\n",
        students.loc[
            "S002":"S004",
            ["name", "score"],
        ].to_string(),
        sep="",
    )

    # Position-based slicing: end position excluded.
    print(
        "\nPosition slice 1:4 (end excluded):\n",
        students.iloc[
            1:4,
            [0, 2],
        ].to_string(),
        sep="",
    )

    # Handle nonexistent student IDs.
    try:
        _ = students.loc["S999"]

    except KeyError:
        print(
            "Unknown student ID handled safely."
        )


def demonstrate_index_operations(
    students: pd.DataFrame,
) -> None:
    """Update scores, align bonuses, and manage indexes."""

    updated = students.copy()

    # Update values using labels and positions.
    updated.at["S003", "score"] = 90
    updated.iat[0, 2] = 85

    # Bonuses are intentionally in a different index order.
    bonus = pd.Series({
        "S004": 3,
        "S001": 2,
        "S003": 4,
        "S002": 1,
    })

    # Align bonuses with the student index.
    # Missing bonuses receive a default value of zero.
    updated["final_score"] = (
        updated["score"]
        + bonus.reindex(
            updated.index,
            fill_value=0,
        )
    ).clip(upper=100)

    print("\n=== Updating and Aligning ===")

    print(
        updated[
            ["name", "score", "final_score"]
        ].to_string()
    )

    # Reindex to include a nonexistent student ID.
    selected = updated.reindex([
        "S001",
        "S003",
        "S999",
    ])

    print(
        "\nReindexed names (missing ID becomes NaN):\n",
        selected["name"].to_string(),
        sep="",
    )

    # Restore the index to an ordinary column.
    restored = updated.reset_index()

    print(
        "\nColumns after reset_index:",
        restored.columns.tolist()
    )

    # Create a hierarchical index.
    course_index = restored.set_index([
        "course",
        "student_id",
    ]).sort_index()

    # Select students enrolled in Python.
    python_students = course_index.loc[
        "Python",
        ["name", "final_score"],
    ]

    print(
        "\nMultiIndex Python students:\n",
        python_students.to_string(),
        sep="",
    )


def main() -> None:
    """Run Pandas indexing demonstrations."""
    students = create_student_data()
    demonstrate_selection(students)
    demonstrate_index_operations(students)


if __name__ == "__main__":
    main()