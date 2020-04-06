def sum_of_pairs_in_list(array, number):
    # find all pairs in the list which sum up to 'number'

    seek = {}
    pairs = []

    for i in range(len(array)):
        value = array[i]
        if value in seek:
            pairs.append((value, number - value))
        else:
            seek[number - value] = 1

    return pairs


if __name__ == "__main__":
    print(sum_of_pairs_in_list([1, 2, 3, 4, 5, 6, 7, 8, 9], 10))
    print(sum_of_pairs_in_list(list(range(100)), 23))
