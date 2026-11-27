
# Decision Trees and Random Forests

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


def main():
    # Load Iris dataset
    iris = load_iris()

    X = iris.data
    y = iris.target

    # Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    print("DECISION TREE CLASSIFIER")
    print("------------------------")

    # Create Decision Tree model
    decision_tree = DecisionTreeClassifier(
        max_depth=4,
        random_state=42
    )

    # Train the model
    decision_tree.fit(X_train, y_train)

    # Predictions
    dt_predictions = decision_tree.predict(X_test)

    dt_accuracy = accuracy_score(y_test, dt_predictions)

    print("Decision Tree Accuracy:",
          round(dt_accuracy * 100, 2), "%")

    print("\nRANDOM FOREST CLASSIFIER")
    print("-----------------------")

    # Create Random Forest model
    random_forest = RandomForestClassifier(
        n_estimators=200,
        random_state=42
    )

    # Train the model
    random_forest.fit(X_train, y_train)

    # Predictions
    rf_predictions = random_forest.predict(X_test)

    rf_accuracy = accuracy_score(y_test, rf_predictions)

    print("Random Forest Accuracy:",
          round(rf_accuracy * 100, 2), "%")

    # Compare both models
    print("\nMODEL COMPARISON")
    print("----------------")

    print("Decision Tree:", round(dt_accuracy * 100, 2), "%")
    print("Random Forest:", round(rf_accuracy * 100, 2), "%")

    # Display feature importance
    print("\nFEATURE IMPORTANCE")
    print("------------------")

    importance = random_forest.feature_importances_

    sorted_features = sorted(
        zip(iris.feature_names, importance),
        key=lambda item: item[1],
        reverse=True
    )

    for feature, score in sorted_features:
        print(feature, ":", round(score, 4))


if __name__ == "__main__":
    main()
