def jumping_clouds(array, jump):
    """
    https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem
    :param array:
    :param jump:
    :return:
    """
    return 100 - sum([1 + 2 * array[i] for i in range(0, len(array), jump)])


if __name__ == "__main__":
    print(jumping_clouds([0, 0, 1, 0, 0, 1, 1, 0], 2))
    print(jumping_clouds([0, 0, 1, 0], 2))
    print(jumping_clouds([1, 1, 1, 0, 1, 1, 0, 0, 0, 0], 3))
