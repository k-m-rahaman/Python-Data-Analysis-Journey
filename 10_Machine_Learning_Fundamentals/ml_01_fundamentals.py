
# Machine Learning Fundamentals

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


def main():
    # Load the Iris dataset
    iris = load_iris()

    X = iris.data
    y = iris.target

    print("MACHINE LEARNING FUNDAMENTALS")
    print("-----------------------------")

    print("Dataset name:", iris.DESCR.splitlines()[0])
    print("Total samples:", len(X))
    print("Total features:", len(iris.feature_names))
    print("Feature names:", iris.feature_names)
    print("Target classes:", iris.target_names)

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    print("\nTraining samples:", len(X_train))
    print("Testing samples:", len(X_test))

    # Create a Machine Learning model
    model = DecisionTreeClassifier(random_state=42)

    # Train the model
    model.fit(X_train, y_train)

    # Make predictions
    predictions = model.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, predictions)

    print("\nModel:", "Decision Tree Classifier")
    print("Accuracy:", round(accuracy * 100, 2), "%")


if __name__ == "__main__":
    main()
