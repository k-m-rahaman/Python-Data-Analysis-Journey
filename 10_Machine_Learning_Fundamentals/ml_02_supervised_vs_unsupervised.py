
# Supervised vs Unsupervised Learning

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
from sklearn.metrics import silhouette_score, adjusted_rand_score


def main():
    iris = load_iris()

    X = iris.data
    y = iris.target

    print("SUPERVISED LEARNING")
    print("-------------------")

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    # Supervised Learning: KNN
    supervised_model = make_pipeline(
        StandardScaler(),
        KNeighborsClassifier(n_neighbors=5)
    )

    supervised_model.fit(X_train, y_train)

    predictions = supervised_model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    print("Algorithm: K-Nearest Neighbors")
    print("Accuracy:", round(accuracy * 100, 2), "%")

    print("\nUNSUPERVISED LEARNING")
    print("---------------------")

    # Scale the complete dataset for clustering
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Unsupervised Learning: K-Means
    unsupervised_model = KMeans(
        n_clusters=3,
        random_state=42,
        n_init=10
    )

    clusters = unsupervised_model.fit_predict(X_scaled)

    print("Algorithm: K-Means Clustering")
    print("Number of clusters:", len(set(clusters)))

    # Evaluate clusters against known labels
    print(
        "Silhouette Score:",
        round(silhouette_score(X_scaled, clusters), 3)
    )

    print(
        "Adjusted Rand Score:",
        round(adjusted_rand_score(y, clusters), 3)
    )


if __name__ == "__main__":
    main()
