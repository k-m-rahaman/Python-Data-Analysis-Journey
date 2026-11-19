
"""
File: 02_seaborn_visualization.py
Topic: Seaborn Statistical Visualization

Description:
    Demonstrates statistical visualization using
    Seaborn and Pandas.

Author: Kazi Mustafijur Rahaman
"""

from pathlib import Path

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def create_visualizations():

    print("=" * 55)
    print("SEABORN STATISTICAL VISUALIZATION")
    print("=" * 55)

    # Student performance dataset.

    students = pd.DataFrame({

        "department": [
            "AI", "AI", "AI", "AI",
            "CSE", "CSE", "CSE", "CSE",
            "ECE", "ECE", "ECE", "ECE"
        ],

        "score": [
            78, 85, 92, 88,
            72, 75, 80, 83,
            68, 74, 77, 81
        ],

        "study_hours": [
            2, 3, 5, 4,
            1, 2, 3, 4,
            1, 2, 3, 4
        ]
    })

    sns.set_theme(style="whitegrid")

    # Create dashboard.

    fig, axes = plt.subplots(
        2, 2,
        figsize=(12, 9)
    )

    # 1. Count plot.

    sns.countplot(
        data=students,
        x="department",
        ax=axes[0, 0]
    )

    axes[0, 0].set_title("Students by Department")

    # 2. Box plot.

    sns.boxplot(
        data=students,
        x="department",
        y="score",
        ax=axes[0, 1]
    )

    axes[0, 1].set_title("Score Distribution by Department")

    # 3. Violin plot.

    sns.violinplot(
        data=students,
        x="department",
        y="score",
        inner="quartile",
        ax=axes[1, 0]
    )

    axes[1, 0].set_title("Department Score Distribution")

    # 4. Histogram with KDE.

    sns.histplot(
        data=students,
        x="score",
        bins=8,
        kde=True,
        ax=axes[1, 1]
    )

    axes[1, 1].set_title("Overall Score Distribution")

    fig.suptitle(
        "Student Performance Analysis",
        fontsize=16
    )

    fig.tight_layout()

    # Save chart.

    output_dir = Path(__file__).resolve().parent / "outputs"
    output_dir.mkdir(exist_ok=True)

    output_file = output_dir / "02_seaborn_analysis.png"

    fig.savefig(
        output_file,
        dpi=150,
        bbox_inches="tight"
    )

    # Statistical summary.

    department_means = students.groupby(
        "department"
    )["score"].mean()

    print(f"\nStudents analyzed: {len(students)}")

    print(
        f"Overall average score: "
        f"{students['score'].mean():.2f}"
    )

    print("\nDepartment averages:")

    for department, average in department_means.items():

        print(f"{department}: {average:.2f}")

    print(
        f"\nHighest performing department: "
        f"{department_means.idxmax()}"
    )

    print(f"Chart saved: outputs/{output_file.name}")

    plt.show()
    plt.close(fig)


if __name__ == "__main__":
    create_visualizations()
