
"""
File: 03_correlation_heatmaps.py
Topic: Correlation Analysis and Heatmaps

Description:
    Analyzes relationships between student performance
    variables using correlation matrices and heatmaps.

Author: Kazi Mustafijur Rahaman
"""

from pathlib import Path

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def analyze_correlations():

    print("=" * 55)
    print("CORRELATION ANALYSIS")
    print("=" * 55)

    # Student performance dataset.

    students = pd.DataFrame({

        "study_hours": [
            1, 2, 3, 4, 5,
            6, 7, 8, 9, 10
        ],

        "attendance": [
            55, 60, 58, 65, 70,
            68, 75, 80, 78, 90
        ],

        "assignment_score": [
            50, 55, 53, 60, 65,
            63, 70, 75, 74, 88
        ],

        "previous_score": [
            48, 52, 50, 58, 62,
            61, 68, 72, 70, 85
        ],

        "final_score": [
            52, 56, 55, 62, 67,
            65, 73, 78, 76, 90
        ]
    })

    # Calculate correlation matrix.

    correlation = students.corr()

    print("\nCORRELATION MATRIX")

    print(correlation.round(2))

    # Find correlations with final score.

    score_correlation = correlation[
        "final_score"
    ].drop("final_score")

    score_correlation = score_correlation.sort_values(
        ascending=False
    )

    print("\nCORRELATION WITH FINAL SCORE")

    for feature, value in score_correlation.items():

        print(f"{feature}: {value:.3f}")

    # Identify strongest relationship.

    strongest_feature = score_correlation.idxmax()

    print(
        f"\nStrongest positive relationship: "
        f"{strongest_feature}"
    )

    # Create heatmap.

    plt.figure(figsize=(10, 7))

    sns.heatmap(
        correlation,
        annot=True,
        cmap="coolwarm",
        vmin=-1,
        vmax=1,
        center=0,
        fmt=".2f",
        square=True,
        linewidths=0.5
    )

    plt.title(
        "Student Performance Correlation Heatmap",
        fontsize=14
    )

    plt.tight_layout()

    # Save heatmap.

    output_dir = Path(__file__).resolve().parent / "outputs"
    output_dir.mkdir(exist_ok=True)

    output_file = output_dir / "03_correlation_heatmap.png"

    plt.savefig(
        output_file,
        dpi=150,
        bbox_inches="tight"
    )

    print(f"\nHeatmap saved: outputs/{output_file.name}")

    plt.show()
    plt.close()


if __name__ == "__main__":
    analyze_correlations()
