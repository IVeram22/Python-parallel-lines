import unittest
from enum import Enum


class Direction(Enum):
    Left = "left"
    Right = "right"


def parallel_lines(matrix: list, direction: Direction):
    n = len(matrix)

    if n == 0:
        return

    m = len(matrix[0])
    result = ""
    if direction is Direction.Right:
        row = n - 1             # start row
        column = 0              # start column
        row_shift = -1          # line shift
        column_shift = 1        # column shift
        k = 0                   # start coefficient
        s_k = 1                 # coefficient shift for column
    else:
        row = n - 1
        column = m - 1
        row_shift = -1
        column_shift = -1
        k = m - 1
        s_k = -1

    for i in range(n*m):
        print(matrix[row][column])
        result += "{} ".format(matrix[row][column])

        if i == 0:
            row += row_shift
            if direction is Direction.Right:
                column = 0
            else:
                column = m - 1
            row_shift *= -1
        else:
            row += row_shift
            column += column_shift

        if row == n:
            row = 0
            column = k
            k += s_k

        if column == m:
            column = m - 1
            row = 0

        if column == -1:
            column = 0
            row = 0

    return result


class Test(unittest.TestCase):
    def test_parallel_lines_empty_matrix(self):
        matrix = []
        print(matrix)
        result = parallel_lines(matrix, Direction.Right) is None
        print("Assert True = {}".format(result))
        self.assertTrue(result)

    def test_parallel_lines_right_NxM(self):
        print("Right NxM")
        matrix = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15]
        ]
        print(matrix)
        result = parallel_lines(matrix, Direction.Right) == "11 6 12 1 7 13 2 8 14 3 9 15 4 10 5 "
        print("Assert True = {}".format(result))
        self.assertTrue(result)

    def test_parallel_lines_left_NxM(self):
        print("Left NxM")
        matrix = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15]
        ]
        print(matrix)
        result = parallel_lines(matrix, Direction.Left) == "15 10 14 5 9 13 4 8 12 3 7 11 2 6 1 "
        print("Assert True = {}".format(result))
        self.assertTrue(result)

    def test_parallel_lines_right_NxN(self):
        print("Right NxN")
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        print(matrix)
        result = parallel_lines(matrix, Direction.Right) == "7 4 8 1 5 9 2 6 3 "
        print("Assert True = {}".format(result))
        self.assertTrue(result)

    def test_parallel_lines_left_NxN(self):
        print("Left NxN")
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        print(matrix)
        result = parallel_lines(matrix, Direction.Left) == "9 6 8 3 5 7 2 4 1 "
        print("Assert True = {}".format(result))
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
