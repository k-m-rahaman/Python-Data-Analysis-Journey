
"""
File: 04_pairplot_jointplot.py
Topic: Pair Plots and Joint Plots

Description:
    Explores relationships between student performance
    variables using Seaborn pair plots and joint plots.

Author: Kazi Mustafijur Rahaman
"""

from pathlib import Path

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def create_pairplot_and_jointplot():

    print("=" * 55)
    print("PAIR PLOT AND JOINT PLOT ANALYSIS")
    print("=" * 55)

    # Student dataset.

    students = pd.DataFrame({

        "study_hours": [
            1, 2, 2, 3, 3, 4,
            4, 5, 5, 6, 6, 7
        ],

        "attendance": [
            60, 65, 68, 70, 72, 75,
            78, 80, 83, 85, 88, 92
        ],

        "exam_score": [
            50, 55, 58, 60, 63, 67,
            69, 73, 76, 80, 84, 89
        ],

        "sleep_hours": [
            5, 6, 7, 6, 8, 7,
            6, 8, 7, 8, 7, 9
        ]
    })

    # Create performance categories.

    students["performance"] = np.where(
        students["exam_score"] >= 70,
        "High",
        "Developing"
    )

    sns.set_theme(style="whitegrid")

    # Display dataset summary.

    print(f"\nStudents analyzed: {len(students)}")

    print(
        f"Average exam score: "
        f"{students['exam_score'].mean():.2f}"
    )

    print("\nPerformance groups:")

    print(
        students["performance"].value_counts().to_string()
    )

    output_dir = Path(__file__).resolve().parent / "outputs"
    output_dir.mkdir(exist_ok=True)

    # 1. Pair plot.

    pair_grid = sns.pairplot(
        students,
        vars=[
            "study_hours",
            "attendance",
            "exam_score",
            "sleep_hours"
        ],
        hue="performance",
        diag_kind="hist",
        corner=True
    )

    pair_grid.fig.suptitle(
        "Student Performance Pair Plot",
        y=1.02
    )

    pairplot_file = output_dir / "04_pairplot.png"

    pair_grid.savefig(
        pairplot_file,
        dpi=150,
        bbox_inches="tight"
    )

    plt.close(pair_grid.fig)

    # 2. Joint plot.

    joint_grid = sns.jointplot(
        data=students,
        x="study_hours",
        y="exam_score",
        kind="reg",
        height=7
    )

    joint_grid.fig.suptitle(
        "Study Hours vs Exam Score",
        y=1.02
    )

    jointplot_file = output_dir / "04_jointplot.png"

    joint_grid.savefig(
        jointplot_file,
        dpi=150,
        bbox_inches="tight"
    )

    plt.close(joint_grid.fig)

    print("\nVISUALIZATION RESULTS")

    print("Pair plot created successfully.")

    print("Joint plot created successfully.")

    print(
        "Charts saved: outputs/04_pairplot.png "
        "and outputs/04_jointplot.png"
    )


if __name__ == "__main__":
    create_pairplot_and_jointplot()
