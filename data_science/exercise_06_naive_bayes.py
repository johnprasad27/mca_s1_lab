"""Exercise 6: Naive Bayes classification."""

import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB


def main() -> None:
    iris = load_iris()
    x_train, x_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.3, random_state=40,
        stratify=iris.target)
    model = GaussianNB()
    model.fit(x_train, y_train)
    prediction = model.predict(x_test)
    print("Accuracy:", metrics.accuracy_score(y_test, prediction))
    print(metrics.classification_report(
        y_test, prediction, target_names=iris.target_names))

    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.scatter(x_test[:, 0], x_test[:, 1], c=prediction,
                cmap="viridis", edgecolor="k")
    plt.title("Predicted classification")
    plt.xlabel("Sepal length")
    plt.ylabel("Sepal width")
    plt.subplot(1, 2, 2)
    plt.scatter(x_test[:, 0], x_test[:, 1], c=y_test,
                cmap="viridis", edgecolor="k")
    plt.title("Actual classification")
    plt.xlabel("Sepal length")
    plt.ylabel("Sepal width")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
