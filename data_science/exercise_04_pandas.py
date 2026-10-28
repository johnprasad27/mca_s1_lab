"""Exercise 4: Introduction to Pandas."""

import numpy as np
import pandas as pd


def main() -> None:
    print("1. List to Series")
    print(pd.Series([1, 4, 6, 3]))

    print("\n2. Date series")
    print(pd.date_range("2021-05-01", "2021-05-12"))

    print("\n3. Dictionary to DataFrame")
    print(pd.DataFrame({
        "Name": ["Alice", "Bob", "Charlie"],
        "Age": [24, 30, 28],
        "City": ["Delhi", "Mumbai", "Bangalore"],
    }))

    print("\n4. 2D list to DataFrame")
    print(pd.DataFrame([[1, "Alice", 10], [2, "Bob", 15], [3, "Don", 25]],
                       columns=["ID", "Name", "Score"]))

    print("\n5. CSV to DataFrame")
    print(pd.read_csv("medal.csv", delimiter=":"))

    scores = pd.DataFrame([[1, "Alice", 15], [2, "Bob", 15], [3, "Don", 45]],
                          columns=["ID", "Name", "Score"])
    print("\n6. Sort by multiple columns")
    print(scores.sort_values(by=["Score", "Name"], ascending=[False, True]))

    indexed = pd.DataFrame(
        [["Alice", 25, "New York"], ["Bob", 30, "Paris"],
         ["Charlie", 35, "London"]],
        columns=["Name", "Age", "City"], index=["p1", "p2", "p3"])
    print("\n7. Reset custom index")
    print(indexed.reset_index(drop=True))

    print("\n8. First two rows")
    print(indexed.reset_index(drop=True).iloc[:2])

    employees = pd.DataFrame(
        [["Alice", "Teacher", 25000], ["Bob", "Doctor", 55000],
         ["Charlie", "Teacher", 20000], ["Dylan", "Doctor", 35000],
         ["Emma", "Engineer", 65000]],
        columns=["Name", "Job", "Salary"])
    print("\n9. Average salary per occupation")
    print(employees.groupby("Job")["Salary"].mean())

    missing = pd.DataFrame({"A": [1, 2, np.nan, 4], "B": [np.nan, 2, 3, 4]})
    print("\n10. Fill NaN values")
    print(missing.fillna(0))

    profits = pd.DataFrame({"cname": ["A", "B", "C"], "profit": [1000, -500, 0]})
    profits["profit"] = profits["profit"] > 0
    print("\n11. Convert profit to Boolean")
    print(profits)

    employee_data = pd.DataFrame(
        [[101, "John", 30000], [102, "Amith", 35000], [103, "Sona", 20000]],
        columns=["ID", "Name", "Stipend"])
    position_data = pd.DataFrame(
        [[101, "Developer"], [102, "Developer"], [103, "Tester"]],
        columns=["ID", "Position"])
    print("\n12. Merge employee and position data")
    print(pd.merge(employee_data, position_data, on="ID", how="inner"))


if __name__ == "__main__":
    main()
