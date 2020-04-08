def count_distinct_slices(array):
    # https://app.codility.com/programmers/lessons/15-caterpillar_method/count_distinct_slices/
    slices = []
    n = len(array)

    for back_pointer, value in enumerate(array):

        cache = dict()
        move_forward = True
        front_pointer = back_pointer

        while front_pointer < n and move_forward:
            if array[front_pointer] in cache:
                move_forward = False
            else:
                slices.append((back_pointer, front_pointer))
                cache[array[front_pointer]] = 1
                front_pointer += 1

    return len(slices)


if __name__ == "__main__":
    print(count_distinct_slices([3, 4, 5, 5, 2]))
    print(count_distinct_slices(range(1000)))
