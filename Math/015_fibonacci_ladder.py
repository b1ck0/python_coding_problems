def fibonacci_ladder(numbers: list, cutoffs: list) -> list:
    """
    https://app.codility.com/programmers/lessons/13-fibonacci_numbers/ladder/
    :param numbers: number to calculate fibonacci on
    :param cutoffs: cutoffs to shorten the answer
    :return: list of fibonacci(numbers)
    """
    cache_fibonacci = {1: 1, 2: 2}
    max_number = max(numbers) + 1

    for i in range(1, max_number + 1):
        if i not in cache_fibonacci:
            cache_fibonacci[i] = cache_fibonacci[i - 1] + cache_fibonacci[i - 2]

    return [cache_fibonacci[number] % (2 ** exp) for number, exp in zip(numbers, cutoffs)]


if __name__ == "__main__":
    print(fibonacci_ladder([4, 4, 5, 5, 1], [3, 2, 4, 3, 1]))
