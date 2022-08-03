import numpy as np


def load_data(file_name):
    with open(file_name, 'r') as f:
        data = f.readlines()
        data = [e.replace('\n', '') for e in data]
        data = [e.split(' ') for e in data]
        data = [[int(e) for e in l] for l in data]
        data = [l + [0 for i in range(len(data) - len(l))] for l in data]
        data = np.array(data)

    return data


def max_sum_for(row_id, column_id, matrix, cache=None):
    if cache is None:
        cache = {(0, 0): matrix[0, 0]}

    if (row_id, column_id) == (0, 0):
        return matrix[row_id, column_id]
    elif column_id > row_id:
        cache[(row_id, column_id)] = 0
        return cache[(row_id, column_id)]
    elif row_id < 0 or column_id < 0:
        cache[(row_id, column_id)] = 0
        return cache[(row_id, column_id)]

    idx_1, idx_2 = (row_id - 1, column_id - 1), (row_id - 1, column_id)

    if idx_1 in cache and idx_2 in cache:
        cache[(row_id, column_id)] = matrix[row_id, column_id] + max(cache[idx_1], cache[idx_2])
        return cache[(row_id, column_id)]
    elif idx_2 in cache and column_id == 0:
        cache[(row_id, column_id)] = matrix[row_id, column_id] + cache[idx_2]
        return cache[(row_id, column_id)]

    else:
        return matrix[row_id, column_id] + max(max_sum_for(row_id - 1, column_id - 1, matrix, cache),
                                               max_sum_for(row_id - 1, column_id, matrix, cache))


if __name__ == "__main__":
    triangle = load_data('./p018_triangle.txt')
    max_row, max_col = triangle.shape

    end_row_sums = []
    for end_node in range(max_col):
        end_row_sums.append(max_sum_for(max_row - 1, end_node, triangle))
        print(len(end_row_sums))

    print(end_row_sums)
    print(max(end_row_sums))
