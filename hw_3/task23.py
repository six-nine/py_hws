import numpy as np
import random


class HashMixin:
    def good_hash(self):
        # hash = (2^0 * a[0][0] + 2^1 * a[0][1] + 2^2 * a[0][2] + ... + 2^(i + j) % 2^32 * a[i][j]) MOD 2^32
        res = 0
        MOD = 2 ** 32
        cur_deg = 1
        for row in self.data:
            for elem in row:
                res = (res + cur_deg * elem) % MOD
                cur_deg = (cur_deg * 2) % MOD
                if cur_deg == 0:
                    cur_deg = 1

        return res

    def __hash__(self):
        return sum(sum(row) for row in self.data)


class ArithmeticMixin:
    cache = dict()

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

        cache_key = (hash(self), hash(other))
        cached = self.cache.get(cache_key, None)
        if cached:
            return cached

        result = [
            [
                sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                for j in range(other.cols)
            ]
            for i in range(self.rows)
        ]

        self.cache[cache_key] = Matrix(result)

        return Matrix(result)


class FileMixin:
    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for row in self.data:
                file.write(' '.join(map(str, row)) + '\n')


class PrettyMixin:
    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])


class AccessMixin:
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if all(isinstance(row, list) for row in value):
            self._data = value
            self.rows = len(self._data)
            self.cols = len(self._data[0])
        else:
            raise ValueError("Data must be a list of lists")


class Matrix(ArithmeticMixin, FileMixin, PrettyMixin, AccessMixin, HashMixin):
    def __init__(self, data):
        self.data = data


if __name__ == '__main__':
    np.random.seed(0)
    matrix1 = Matrix(np.random.randint(0, 10, (10, 10)).tolist())
    matrix2 = Matrix(np.random.randint(0, 10, (10, 10)).tolist())

    res_add = matrix1 + matrix2
    res_mul = matrix1 * matrix2
    res_matmul = matrix1 @ matrix2

    res_add.save_to_file('./artifacts/3.2/matrix+.txt')
    res_mul.save_to_file('./artifacts/3.2/matrix*.txt')
    res_matmul.save_to_file('./artifacts/3.2/matrix@.txt')

    A = Matrix([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 8, 7, 6],
    ])

    C = Matrix([
        [4, 3, 2, 1],
        [8, 8, 7, 5],
        [9, 6, 7, 6],
    ])

    assert hash(A) == hash(C)

    B = Matrix([
        [1, 1],
        [7, 2],
        [4, 3],
        [9, 5],
    ])

    D = B

    A.save_to_file('./artifacts/3.3/A.txt')
    B.save_to_file('./artifacts/3.3/B.txt')
    C.save_to_file('./artifacts/3.3/C.txt')
    D.save_to_file('./artifacts/3.3/D.txt')

    AB = A @ B
    CD = C @ D

    AB.save_to_file('./artifacts/3.3/AB.txt')
    CD.save_to_file('./artifacts/3.3/CD_wrong.txt')

    ArithmeticMixin.cache = dict()

    CD = C @ D
    CD.save_to_file('./artifacts/3.3/CD.txt')

    with open('./artifacts/3.3/hash.txt', 'w') as f:
        f.write(f"{hash(AB)}, {hash(CD)}")
