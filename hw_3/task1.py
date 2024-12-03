import numpy as np


class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Different dimensions: ({self.rows}, {selg.cols}) != ({other.rows}, {other.cols})")
        result = [
            [self.data[i][j] + other.data[i][j] for j in range(self.cols)] 
            for i in range(self.rows)
        ]

        return Matrix(result)

    def __mul__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Different dimensions: ({self.rows}, {selg.cols}) != ({other.rows}, {other.cols})")
        result = [
            [self.data[i][j] * other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]

        return Matrix(result)

    def __matmul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Incompatible dimensions for matrix multiplication")
        result = [
            [
                sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                for j in range(other.cols)
            ]
            for i in range(self.rows)
        ]
        return Matrix(result)

    def __str__(self):
        return "\n".join(" ".join(str(cell) for cell in row) for row in self.data)

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            file.write(str(self))


def write_matrix_to_file(filename, matrix):
    with open(filename, 'w') as file:
        file.write(str(matrix))


if __name__ == '__main__':
    np.random.seed(0)
    matrix1 = Matrix(np.random.randint(0, 10, (10, 10)))
    matrix2 = Matrix(np.random.randint(0, 10, (10, 10)))

    res_add = matrix1 + matrix2
    res_mul = matrix1 * matrix2
    res_matmul = matrix1 @ matrix2

    write_matrix_to_file('./artifacts/3.1/matrix+.txt', res_add)
    write_matrix_to_file('./artifacts/3.1/matrix*.txt', res_mul)
    write_matrix_to_file('./artifacts/3.1/matrix@.txt', res_matmul)
