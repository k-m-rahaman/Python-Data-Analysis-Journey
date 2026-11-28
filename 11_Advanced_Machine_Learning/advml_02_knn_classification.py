
# K-Nearest Neighbors Classification

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix


def main():
    iris = load_iris()
    X, y = iris.data, iris.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    model = make_pipeline(
        StandardScaler(),
        KNeighborsClassifier(n_neighbors=5)
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    print("K-NEAREST NEIGHBORS")
    print("-------------------")
    print("Number of neighbors:", 5)
    print("Accuracy:", round(accuracy_score(y_test, predictions) * 100, 2), "%")

    print("\nCONFUSION MATRIX")
    print("----------------")
    print(confusion_matrix(y_test, predictions))

    # Predict a new flower
    new_flower = [[5.1, 3.5, 1.4, 0.2]]
    prediction = model.predict(new_flower)

    print("\nNEW FLOWER PREDICTION")
    print("---------------------")
    print("Predicted species:", iris.target_names[prediction[0]])


if __name__ == "__main__":
    main()
