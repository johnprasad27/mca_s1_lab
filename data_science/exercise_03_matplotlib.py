"""Exercise 3: Programs using Matplotlib."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def main() -> None:
    x = np.array([1, 2, 6, 18])
    y = np.array([3, 10, 12, 20])
    plt.figure()
    plt.plot(x, y, linestyle=":", marker=".", markersize=10,
             markerfacecolor="green", markeredgecolor="green", color="red")
    plt.title("Line with marked points")

    temperature = np.array([12, 14, 16, 18, 20, 22, 24])
    sales = np.array([100, 200, 250, 400, 300, 450, 500])
    plt.figure()
    plt.plot(temperature, sales, color="green", marker="*",
             markerfacecolor="red", markeredgecolor="red")
    plt.xlabel("Temperature")
    plt.ylabel("Sales")

    data_file = Path(__file__).with_name("exercise3.3.txt")
    file_x, file_y = [
        np.array(list(map(int, line.strip().split(","))))
        for line in data_file.read_text(encoding="utf-8").splitlines()
    ]
    plt.figure()
    plt.plot(file_x, file_y, marker="*", markeredgecolor="black",
             markerfacecolor="black")
    plt.title("Temperature Information")
    plt.xlabel("Day")
    plt.ylabel("Temperature")

    days = np.arange(1, 6)
    high = np.array([30, 32, 31, 32, 33])
    low = np.array([27, 26, 29, 28, 29])
    plt.figure()
    plt.plot(days, high, color="red", marker=".", label="Highest Temperature")
    plt.plot(days, low, color="blue", marker=".", label="Lowest Temperature")
    plt.xlabel("Day")
    plt.title("Temperature Difference")
    plt.legend()

    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.plot(days, high, color="red", marker=".")
    plt.xlabel("Day")
    plt.ylabel("Temperature (C)")
    plt.title("Highs")
    plt.subplot(1, 2, 2)
    plt.plot(days, low, color="blue", marker=".")
    plt.xlabel("Day")
    plt.ylabel("Temperature (C)")
    plt.title("Lows")
    plt.suptitle("Temperature Difference Over 5 Days")

    languages = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
    popularity = [22.2, 17.6, 8.8, 8, 77, 6.7]
    plt.figure()
    plt.bar(languages, popularity, color="blue")
    plt.title("Programming Languages Popularity")
    plt.figure()
    plt.barh(languages, popularity, color="red")
    plt.title("Programming Languages Popularity")
    plt.figure()
    plt.bar(languages, popularity,
            color=["red", "green", "blue", "orange", "purple", "brown"])

    groups = np.arange(1, 6) * 3
    plt.figure()
    plt.bar(groups - 0.4, [22, 30, 35, 35, 26], 0.4, label="Men")
    plt.bar(groups + 0.4, [25, 22, 30, 35, 29], 0.4, label="Women")
    plt.title("Scores by person")
    plt.legend()

    plt.figure()
    plt.pie([30, 40, 10, 10, 5, 5], labels=languages)

    medal_file = Path(__file__).with_name("medal.csv")
    medal_data = pd.read_csv(medal_file, delimiter=":")
    plt.figure()
    plt.pie(medal_data["Gold_Medal"], labels=medal_data["Country"],
            autopct="%1.1f%%")

    marks_range = np.arange(10, 101, 10)
    plt.figure()
    plt.scatter(marks_range, [88, 92, 80, 89, 100, 80, 60, 100, 80, 34],
                color="red", label="Maths")
    plt.scatter(marks_range, [35, 79, 79, 48, 100, 88, 32, 45, 20, 30],
                color="green", label="Science")
    plt.xlabel("Marks Range")
    plt.title("Math marks vs Science marks")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
