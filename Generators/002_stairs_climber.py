def stairs_climber_generator():
    current, previous = 2, 1

    while True:
        yield current
        current, previous = current + previous, current


if __name__ == "__main__":
    fibonacci_sequence = stairs_climber_generator()

    for i in range(2, 50):
        print(f"n = {i}, n_paths_to_level({i}) = {next(fibonacci_sequence)}")
