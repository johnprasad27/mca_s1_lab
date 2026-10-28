"""Exercise 2: Matrix operations."""

import numpy as np


def read_matrix(order: int) -> np.ndarray:
    values = []
    for row in range(order):
        values.append(
            [int(input(f"Enter element {row},{column}: ")) for column in range(order)]
        )
    return np.array(values)


def main() -> None:
    order = int(input("Enter the order of the matrices: "))
    print("Matrix 1")
    matrix1 = read_matrix(order)
    print("Matrix 2")
    matrix2 = read_matrix(order)

    print("Matrices are:")
    print(matrix1)
    print(matrix2)
    print("Dot product:", np.dot(matrix1, matrix2))
    print("Transpose of matrix 1:", np.transpose(matrix1))
    print("Trace of matrix 1:", np.trace(matrix1))
    print("Rank of matrix 1:", np.linalg.matrix_rank(matrix1))
    print("Determinant of matrix 1:", np.linalg.det(matrix1))
    print("Inverse of matrix 1:", np.linalg.inv(matrix1))
    print("Eigenvalues and eigenvectors of matrix 1:", np.linalg.eig(matrix1))


if __name__ == "__main__":
    main()
