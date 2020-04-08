def abs_distinct(array):
    # https://app.codility.com/programmers/lessons/15-caterpillar_method/abs_distinct/
    # write your code in Python 3.6
    cache = {}

    for element in array:
        cache[abs(element)] = cache.get(abs(element), 0) + 1

    return len(cache)
