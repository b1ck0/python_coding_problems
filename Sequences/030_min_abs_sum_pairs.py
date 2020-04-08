def min_abs_sum_pairs(array):
    # https://app.codility.com/programmers/lessons/15-caterpillar_method/min_abs_sum_of_two/

    n = len(array)
    min_value = float('inf')  # this is what codility expects 2000000000 instead of infinity

    if n < 2:
        return min_value

    array.sort()
    back_pointer, front_pointer = 0, n - 1

    if array[back_pointer] >= 0 and array[front_pointer] >= 0:
        # all positive
        return array[back_pointer] * 2

    if array[back_pointer] <= 0 and array[front_pointer] <= 0:
        # all negative
        return abs(array[front_pointer]) * 2

    while back_pointer <= front_pointer:

        back_value, front_value = array[back_pointer], array[front_pointer]

        # early stopping criteria
        if back_value + front_value == 0:
            return 0

        abs_sum = abs(back_value + front_value)
        min_value = min(min_value, abs_sum)

        if abs(back_value) > abs(front_value):
            back_pointer += 1
        else:
            front_pointer -= 1

    return min_value


if __name__ == "__main__":
    print(min_abs_sum_pairs([1, 4, -3]))
    print(min_abs_sum_pairs([-8, 4, 5, -10, 3]))
