def fibonacci(n, cache=None):

    if cache is None:
        cache = dict()

    if n == 0 or n == 1:
        return 1

    else:
        if n in cache:
            return cache[n]
        else:
            result = fibonacci(n - 1, cache) + fibonacci(n - 2, cache)
            cache[n] = result

            return result


if __name__ == '__main__':
    import timeit

    iterations = 10000
    t = timeit.timeit('fibonacci(120)', number=iterations, globals=globals())

    print(f"mean execution time = {t}, based on {iterations} iterations")
