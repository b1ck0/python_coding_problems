# algorithm from https://www.youtube.com/watch?v=G_UYXzGuqvM
# Professor Thorsten Altenkirch

import numpy as np


def is_possible(row, col, n):
    global grid

    for i in range(9):
        if grid[row][i] == n:
            return False

    for i in range(9):
        if grid[i][col] == n:
            return False

    row0 = (row // 3) * 3
    col0 = (col // 3) * 3

    for i in range(3):
        for j in range(3):
            if grid[row0 + i][col0 + j] == n:
                return False

    return True


def solver():
    global grid

    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for n in range(1, 10):
                    if is_possible(row, col, n):
                        grid[row][col] = n
                        solver()
                        grid[row][col] = 0
                return

    print(np.matrix(grid))
    input("More ?")


if __name__ == "__main__":
    grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print(is_possible(4, 4, 3))
    print(is_possible(4, 4, 5))

    solver()
