"""Exercise 9: Linear regression."""

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score


def main() -> None:
    diabetes_x, diabetes_y = datasets.load_diabetes(return_X_y=True)
    diabetes_x = diabetes_x[:, np.newaxis, 2]
    x_train, x_test = diabetes_x[:-20], diabetes_x[-20:]
    y_train, y_test = diabetes_y[:-20], diabetes_y[-20:]

    model = linear_model.LinearRegression()
    model.fit(x_train, y_train)
    prediction = model.predict(x_test)
    print("Coefficients:", model.coef_)
    print("Intercept:", model.intercept_)
    print("Mean squared error: %.2f" % mean_squared_error(y_test, prediction))
    print("R^2 score: %.2f" % r2_score(y_test, prediction))

    plt.scatter(x_test, y_test, color="black")
    sorted_indices = np.argsort(x_test[:, 0])
    plt.plot(x_test[sorted_indices], prediction[sorted_indices],
             color="blue", linewidth=3)
    plt.xlabel("BMI")
    plt.ylabel("Diabetes progression")
    plt.title("Linear Regression: BMI vs Diabetes Progression")
    plt.show()


if __name__ == "__main__":
    main()
