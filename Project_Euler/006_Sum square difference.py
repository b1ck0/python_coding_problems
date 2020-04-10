# https://www.hackerrank.com/contests/projecteuler/challenges/euler006/problem

def sum_to_n(n):
    # 1+2+3+...+n
    return n * (n + 1) / 2


def sum_square_to_n(n):
    # 1**2 + 2**2 + 3** 2 + ... + n**2
    return n * (n + 1) * (2 * n + 1) / 6


def square_sum_difference(n):
    return int(sum_to_n(n) ** 2 - sum_square_to_n(n))


if __name__ == "__main__":
    print(square_sum_difference(10))
    print(square_sum_difference(100))
