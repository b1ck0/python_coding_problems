def find_missing_element(array):
    # https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/
    # write your code in Python 3.6
    n = len(array)
    sum_to_n = (n + 1) * (n + 2) / 2

    return int(sum_to_n - sum(array))
