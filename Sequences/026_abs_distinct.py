def abs_distinct(array):
    # https://app.codility.com/programmers/lessons/15-caterpillar_method/abs_distinct/
    # write your code in Python 3.6
    cache = {}
    n = 0

    for element in array:
        if abs(element) not in cache:
            cache[abs(element)] = 1
            n += 1
        else:
            cache[abs(element)] += 1

    return n
