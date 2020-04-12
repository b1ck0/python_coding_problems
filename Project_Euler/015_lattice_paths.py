from functools import reduce


def product(a, b):
    return a * b


def factorial(k):
    return reduce(product, range(1, k + 1))


def num_paths(m, n):
    return factorial(m + n) / (factorial(m) * factorial(n))


if __name__ == "__main__":
    print(num_paths(20, 20))
    print(num_paths(500, 500))
