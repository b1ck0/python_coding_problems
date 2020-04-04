def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    import timeit

    iterations = 10000
    t = timeit.timeit('fibonacci(120)', number=iterations, globals=globals())

    print(f"mean execution time = {t}, based on {iterations} iterations")
