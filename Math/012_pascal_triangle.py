def pascal_triangle(n):
    """
    https://www.hackerrank.com/challenges/ncr-table/problem
    (n choose k) = fact(n)/fact(k)fact(n-k)
    :param n:
    :param k:
    :return: [ (n choose k) ] (if number is very big return the last 9 digits only)
    """

    cache = {
        (n, 0): 1
    }

    for k in range(0, n + 1):
        if (n, k) in cache:
            cache[(n, k + 1)] = int(cache[(n, k)] * (n - k) / (k + 1))

    # return cache
    m = 10**9
    return [cache[(n, k)] % m for k in range(n + 1)]


if __name__ == "__main__":
    print(pascal_triangle(2))
    print(pascal_triangle(3))
    print(pascal_triangle(4))
    print(pascal_triangle(5))
    print(pascal_triangle(879))
