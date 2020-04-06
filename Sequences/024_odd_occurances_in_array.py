def odd_occurance(array):
    """
    https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/
    :param array:
    :return:
    """
    result = 0

    for element in array:
        result ^= element

    return result
