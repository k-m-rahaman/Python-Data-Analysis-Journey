
# Support Vector Machines (SVM)

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report


def main():
    data = load_breast_cancer()
    X, y = data.data, data.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    # Scaling is important for SVM
    model = make_pipeline(
        StandardScaler(),
        SVC(kernel="rbf", C=1.0)
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    print("SUPPORT VECTOR MACHINE")
    print("----------------------")
    print("Training samples:", len(X_train))
    print("Testing samples:", len(X_test))
    print("Kernel: RBF")
    print("Accuracy:", round(accuracy_score(y_test, predictions) * 100, 2), "%")

    print("\nCLASSIFICATION REPORT")
    print("---------------------")
    print(classification_report(
        y_test,
        predictions,
        target_names=data.target_names
    ))


if __name__ == "__main__":
    main()
