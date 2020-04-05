def rotate_right(array, n_shifts, debug_ids):
    """
    https://www.hackerrank.com/challenges/circular-array-rotation/problem
    :param array: list
    :param n_shifts: number of right rotations
    :param debug_ids: list of indices to report after all rotations array[debug_ids] = ?
    :return: rotated_array[[debug_ids]]
    """
    if not isinstance(debug_ids, list):
        debug_ids = []

    array = array[-(n_shifts % len(array)):] + array[:-(n_shifts % len(array))]

    return [array[i] for i in debug_ids]


if __name__ == "__main__":
    print(rotate_right([3, 4, 5], 2, [1, 2]))
    print(rotate_right([1, 2, 3], 2, [0, 1, 2]))
    print(rotate_right([1, 2, 3], 2, []))
