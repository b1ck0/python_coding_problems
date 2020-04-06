def binary_search_iterative(array, element):
    """
    :param array: must be sorted
    :param element: element we want to find
    :return: returns True/False in O(log n)
    """
    left = 0
    right = len(array) - 1
    found = False

    while left <= right and not found:
        i = (left + right) // 2
        if array[i] == element:
            found = True
        else:
            if element < array[i]:
                right = i - 1
            else:
                left = i + 1

    return found


def binary_search_recursive(array, element):
    """
    :param array: must be sorted
    :param element: element we want to find
    :return: returns True/False in O(log n)
    """
    if len(array) == 0:
        return False

    i = len(array) // 2

    if array[i] == element:
        return True
    elif array[i] > element:
        return binary_search_recursive(array[:i], element)
    else:
        return binary_search_recursive(array[i + 1:], element)


if __name__ == "__main__":
    print(binary_search_recursive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))
    print(binary_search_recursive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11))
    print(binary_search_recursive([1, 2, 3, 4, 5, 6, 7, 8, 8, 10], 9))
    print(binary_search_recursive([1, 2, 3, 4, 5, 6, 7, 8, 8, 10], 8))
    print(binary_search_recursive([1, 2, 3, 4, 5, 6, 7, 8, 10], 8))
    print(binary_search_recursive([1, 3, 6, 7, 2, 3, 0, 8, 9, 6, 7, 8, 1, 2, 22], 21))
    print(binary_search_recursive([1, 3, 6, 7, 2, 3, 0, 8, 9, 6, 7, 8, 1, 2, 22], 22))
    print("=" * 80)
    print(binary_search_iterative([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))
    print(binary_search_iterative([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11))
    print(binary_search_iterative([1, 2, 3, 4, 5, 6, 7, 8, 8, 10], 9))
    print(binary_search_iterative([1, 2, 3, 4, 5, 6, 7, 8, 8, 10], 8))
    print(binary_search_iterative([1, 3, 6, 7, 2, 3, 0, 8, 9, 6, 7, 8, 1, 2, 22], 21))
    print(binary_search_iterative([1, 3, 6, 7, 2, 3, 0, 8, 9, 6, 7, 8, 1, 2, 22], 22))
