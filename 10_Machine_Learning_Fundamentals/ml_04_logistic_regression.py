
# Logistic Regression

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix, classification_report


def main():
    # Load Breast Cancer dataset
    data = load_breast_cancer()

    X = data.data
    y = data.target

    # Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    # Create Logistic Regression model
    model = make_pipeline(
        StandardScaler(),
        LogisticRegression(max_iter=2000, random_state=42)
    )

    # Train the model
    model.fit(X_train, y_train)

    # Make predictions
    predictions = model.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, predictions)

    print("LOGISTIC REGRESSION")
    print("-------------------")

    print("Total samples:", len(X))
    print("Total features:", len(data.feature_names))
    print("Classes:", data.target_names)

    print("\nModel Accuracy:", round(accuracy * 100, 2), "%")

    print("\nCONFUSION MATRIX")
    print("----------------")
    print(confusion_matrix(y_test, predictions))

    print("\nCLASSIFICATION REPORT")
    print("---------------------")
    print(
        classification_report(
            y_test,
            predictions,
            target_names=data.target_names,
            zero_division=0
        )
    )


if __name__ == "__main__":
    main()
