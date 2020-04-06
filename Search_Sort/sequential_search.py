def sequential_search(array, element, ordered=False):
    """
    :param ordered: sorted ?
    :param array: list
    :param element: element we want to find
    :return: returns True/False in O(n)
    """
    for i in range(len(array)):
        if array[i] == element:
            return True
        if ordered:
            if array[i] > element:
                return False

    return False


if __name__ == "__main__":
    print(sequential_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, True))
    print(sequential_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11, True))
    print(sequential_search([1, 2, 3, 4, 5, 6, 7, 8, 8, 10], 9, True))
    print(sequential_search([1, 2, 3, 4, 5, 6, 7, 8, 8, 10], 8, True))
    print(sequential_search([1, 3, 6, 7, 2, 3, 0, 8, 9, 6, 7, 8, 1, 2, 22], 21))
    print(sequential_search([1, 3, 6, 7, 2, 3, 0, 8, 9, 6, 7, 8, 1, 2, 22], 22))
