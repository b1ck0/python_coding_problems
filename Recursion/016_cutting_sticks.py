def cutting_sticks(array):
    """
    https://www.hackerrank.com/challenges/cut-the-sticks/problem
    :param array:
    :return:
    """

    if len(array) == 1:
        return [1]
    else:
        if sum(array)/len(array) == array[0]:
            return [len(array)]
        else:
            return [len(array)] + cutting_sticks([i - min(array) for i in array if i - min(array) > 0])


if __name__ == "__main__":
    print(cutting_sticks([5, 4, 4, 2, 2, 8]))
    print(cutting_sticks([1, 2, 3, 4, 3, 3, 2, 1]))
    print(cutting_sticks([8, 8, 14, 10, 3, 5, 14, 12]))
