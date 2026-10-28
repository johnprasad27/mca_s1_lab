"""Exercise 8: K-means clustering."""

import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score, normalized_mutual_info_score


def main() -> None:
    iris = datasets.load_iris()
    features = iris.data[:, :2]
    kmeans = KMeans(n_clusters=3, random_state=21, n_init=10)
    kmeans.fit(features)
    labels = kmeans.labels_

    plt.subplot(1, 2, 1)
    plt.scatter(features[:, 0], features[:, 1], c=iris.target,
                cmap="prism", edgecolor="k")
    plt.title("Actual")
    plt.xlabel("Sepal Length")
    plt.ylabel("Sepal Width")
    plt.subplot(1, 2, 2)
    plt.scatter(features[:, 0], features[:, 1], c=labels,
                cmap="jet", edgecolor="k")
    plt.title("Predicted")
    plt.xlabel("Sepal Length")
    plt.ylabel("Sepal Width")
    plt.tight_layout()
    plt.show()

    print(f"Adjusted Rand Index (ARI): {adjusted_rand_score(iris.target, labels):.3f}")
    print(f"Normalized Mutual Information (NMI): "
          f"{normalized_mutual_info_score(iris.target, labels):.3f}")


if __name__ == "__main__":
    main()
