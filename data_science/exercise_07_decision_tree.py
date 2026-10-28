"""Exercise 7: Decision tree classification."""

import matplotlib.pyplot as plt
from sklearn import metrics, tree
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


def main() -> None:
    iris = load_iris()
    x_train, x_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.3, random_state=42,
        stratify=iris.target)
    classifier = DecisionTreeClassifier(
        criterion="entropy", max_depth=4, min_samples_leaf=2,
        random_state=42)
    classifier.fit(x_train, y_train)
    prediction = classifier.predict(x_test)
    print(metrics.classification_report(
        y_test, prediction, target_names=iris.target_names))

    plt.figure(figsize=(16, 10))
    tree.plot_tree(
        classifier, feature_names=iris.feature_names,
        class_names=iris.target_names, filled=True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
