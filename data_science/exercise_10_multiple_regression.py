"""Exercise 10: Multiple regression."""

import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score


def main() -> None:
    diabetes_x, diabetes_y = datasets.load_diabetes(return_X_y=True)
    diabetes_x = diabetes_x[:, [0, 2]]
    x_train, x_test = diabetes_x[:-20], diabetes_x[-20:]
    y_train, y_test = diabetes_y[:-20], diabetes_y[-20:]

    model = linear_model.LinearRegression()
    model.fit(x_train, y_train)
    prediction = model.predict(x_test)
    print("Coefficients:", model.coef_)
    print("Intercept:", model.intercept_)
    print("Mean squared error: %.2f" % mean_squared_error(y_test, prediction))
    print("R^2 score: %.2f" % r2_score(y_test, prediction))

    plt.figure(figsize=(14, 5))
    for index, (feature, color, marker) in enumerate(
        [(0, "blue", "o"), (1, "green", "D")], start=1
    ):
        plt.subplot(1, 2, index)
        plt.scatter(x_test[:, feature], y_test, color="red",
                    marker="o", label="Actual", alpha=0.7)
        plt.scatter(x_test[:, feature], prediction, color=color,
                    marker=marker, label="Predicted", alpha=0.7)
        plt.xlabel(f"Feature {0 if feature == 0 else 2}")
        plt.ylabel("Diabetes Progression")
        plt.title("Feature vs Target")
        plt.legend()
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(8, 6))
    plt.scatter(y_test, prediction, color="purple", marker="^",
                label="Predicted vs Actual", alpha=0.7)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()],
             "r--", label="Ideal Fit")
    plt.xlabel("Actual Diabetes Progression")
    plt.ylabel("Predicted Diabetes Progression")
    plt.title("Actual vs Predicted Diabetes Progression")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
