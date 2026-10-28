"""Exercise 1: Introduction to NumPy."""

import numpy as np


def main() -> None:
    fahrenheit = np.array([100, 98.4, 91.50, 99.78, 101.5])
    centigrade = (fahrenheit - 32) * (5 / 9)
    print("Fahrenheit values:", fahrenheit)
    print("Centigrade values:", centigrade)

    values = np.array([23, 55, 29, 56, 28, 86, 12])
    print("\nArray:", values)
    print("Mean:", np.mean(values))
    print("Variance:", np.var(values))
    print("Standard deviation:", np.std(values))

    degrees = np.array([32, 40, 180, 360, 45, 93])
    print("\nDegrees:", degrees)
    print("Radian values:", np.deg2rad(degrees))

    values = np.array([12, 34, 6, 28, 46, 90, 3])
    print("\nArray:", values)
    print("Difference:", np.diff(values))

    complex_values = np.array([7 + 5j, 4 + 3j, 12 + 2j, 1 + 8j, 1 + 9j])
    print("\nArray before sorting:", complex_values)
    print("After sorting:", np.sort(complex_values))

    random_values = np.random.default_rng(42).integers(-40, 40, size=10)
    print("\nRandom array:", random_values)
    print("Elements greater than 4:", random_values[random_values > 4])

    search_values = np.array([-10, -10, -2, 29, 29, 39, 8, 30, 26, 2])
    number = int(input("\nEnter a number to search: "))
    if np.any(search_values == number):
        print("Number is present in the array")
    else:
        print("Number is not present in the array")

    file_values = np.array([4, 5, 4, 6, 11, 2235, 56], dtype=float)
    np.savetxt("exercise1_array.txt", file_values)
    print("\nArray loaded from exercise1_array.txt:")
    print(np.loadtxt("exercise1_array.txt"))

    print("\nEven integers from 30 to 60:", np.arange(30, 61, 2))

    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("\nArray:", matrix)
    print("Sum of elements:", np.sum(matrix))
    print("Column-wise sum:", np.sum(matrix, axis=0))
    print("Row-wise sum:", np.sum(matrix, axis=1))


if __name__ == "__main__":
    main()
