def modified_fibonacci(t1, t2, n, cache=None):
    """
        https://www.hackerrank.com/challenges/fibonacci-modified/problem
        t(n+2) = t(n) + (tn+1)**2
    """
    if cache is None:
        cache = dict()

    if n == 1:
        return t1
    elif n == 2:
        return t2
    else:
        if n in cache:
            return cache[n]
        else:
            cache[n] = modified_fibonacci(t1, t2, n - 2) + modified_fibonacci(t1, t2, n - 1) ** 2
            return cache[n]


if __name__ == "__main__":
    print(modified_fibonacci(0, 1, 5))
