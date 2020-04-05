def most_frequent_element(array):
    """
    :param array: list
    :return: the most frequent element (if there is a tie return the smaller element)
    """
    value_frequency = dict()

    for element in array:
        if element not in value_frequency:
            value_frequency[element] = 1
        else:
            value_frequency[element] += 1

    descending_value_frequencies = sorted(value_frequency.items(), reverse=True)
    most_frequent_pair = descending_value_frequencies[0]

    for pair in descending_value_frequencies[1:]:
        if pair[1] >= most_frequent_pair[1] and pair[0] < most_frequent_pair[0]:
            most_frequent_pair = pair

    return most_frequent_pair[0]


if __name__ == "__main__":
    print(most_frequent_element([1, 1, 1, 2, 3, 4, 5, 4, 4, 3, 2, 4, 2, 1, 2, 1, 1, 2, 3, 4, 5]))
