
"""
File: 05_feature_selection.py
Topic: Feature Selection Techniques

Description:
Selects useful features from a student performance
dataset using variance and correlation analysis.

Author: Kazi Mustafijur Rahaman
"""

import pandas as pd

from sklearn.feature_selection import VarianceThreshold


def create_student_data() -> pd.DataFrame:
    """Create student performance dataset."""

    return pd.DataFrame({
        "study_hours": [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10
        ],
        "attendance_rate": [
            40, 45, 50, 55, 60, 80, 85, 90, 95, 100
        ],
        "assignment_score": [
            20, 30, 25, 40, 35, 65, 70, 60, 80, 90
        ],
        "random_feature": [
            9, 1, 8, 2, 7, 3, 6, 4, 5, 0
        ],
        "constant_feature": [1] * 10,
        "passed_exam": [
            0, 0, 0, 0, 0, 1, 1, 1, 1, 1
        ]
    })


def select_features(data: pd.DataFrame):
    """Select important features."""

    X = data.drop(columns=["passed_exam"])
    y = data["passed_exam"]

    # Remove features with zero variance
    variance_selector = VarianceThreshold(
        threshold=0.0
    )

    filtered_values = variance_selector.fit_transform(X)

    selected_names = (
        variance_selector.get_feature_names_out()
    )

    filtered_data = pd.DataFrame(
        filtered_values,
        columns=selected_names
    )

    removed_features = [
        column for column in X.columns
        if column not in selected_names
    ]

    # Rank features by absolute correlation
    correlation_scores = (
        filtered_data
        .corrwith(y)
        .abs()
        .sort_values(ascending=False, kind="stable")
    )

    # Select the three most relevant features
    top_features = correlation_scores.head(3)

    return removed_features, top_features


def main():
    print("=" * 55)
    print("FEATURE SELECTION TECHNIQUES")
    print("=" * 55)

    data = create_student_data()

    print("\nOriginal Dataset:")
    print(data.to_string(index=False))

    removed, selected = select_features(data)

    print("\nRemoved Constant Features:")
    print(removed)

    print("\nTop 3 Selected Features:")

    for feature, score in selected.items():
        print(f"{feature}: {score:.3f}")


if __name__ == "__main__":
    main()
