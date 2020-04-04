def fibonacci_generator():
    current, previous = 0, 1
    while True:
        yield current
        current, previous = current + previous, current


if __name__ == "__main__":
    fibonacci_sequence = fibonacci_generator()

    for i in range(0, 11):
        print(f"n = {i}, fib({i}) = {next(fibonacci_sequence)}")
