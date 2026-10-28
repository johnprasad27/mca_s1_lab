"""Exercise 5: K-nearest-neighbours classification."""

import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


def main() -> None:
    iris = load_iris()
    x_train, x_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.25, random_state=42,
        stratify=iris.target)
    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(x_train, y_train)
    prediction = model.predict(x_test)
    print("Accuracy:", metrics.accuracy_score(y_test, prediction))

    sample = [[2, 2, 2, 2]]
    predicted_class = model.predict(sample)[0]
    print("New sample belongs to", iris.target_names[predicted_class])

    plt.subplot(1, 2, 1)
    plt.scatter(x_test[:, 0], x_test[:, 1], c=prediction)
    plt.title("Predicted classification")
    plt.xlabel("Sepal length")
    plt.ylabel("Sepal width")
    plt.subplot(1, 2, 2)
    plt.scatter(x_test[:, 0], x_test[:, 1], c=y_test)
    plt.title("Actual classification")
    plt.xlabel("Sepal length")
    plt.ylabel("Sepal width")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
