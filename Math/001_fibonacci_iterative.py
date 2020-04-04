def fibonacci(n):
    sequence = []

    for i in range(n):
        if i == 0 or i == 1:
            sequence.append(i)
        else:
            sequence.append(sequence[i - 1] + sequence[i - 2])

    return sequence


if __name__ == '__main__':
    import timeit

    iterations = 10000
    t = timeit.timeit('fibonacci(120)', number=iterations, globals=globals())

    print(f"mean execution time = {t}, based on {iterations} iterations")
