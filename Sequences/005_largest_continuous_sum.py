def largest_continuous_sum(array: list) -> int:
    max_sum = 0
    max_start = None
    max_end = None

    for window_size in range(1, len(array)):
        for i in range(len(array)):
            start = i
            end = i + window_size
            if end <= len(array):
                s = sum(array[start:end])
                if s > max_sum:
                    max_sum = s
                    max_start = start
                    max_end = end
                else:
                    pass

    print(f"sum(array[{max_start},{max_end}] = {max_sum}")
    return max_sum


def kadane_algorithm(array: list) -> int:
    if len(array) == 0:
        return 0

    max_sum = current_sum = array[0]

    for number in array[1:]:
        current_sum = max(current_sum, current_sum + number)
        max_sum = max(max_sum, current_sum)

    return max_sum


def kadane_algorithm_with_bounds(array: list) -> float:
    if len(array) == 0:
        return 0

    max_so_far = float('-inf')
    max_ending_here = 0
    start = 0
    end = 0
    s = 0

    for i in range(len(array)):
        max_ending_here += array[i]

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i

        if max_ending_here < 0:
            max_ending_here = 0
            s = i + 1

    print(f"sum(array[{start},{end}] = {max_so_far}")
    return max_so_far


if __name__ == "__main__":
    from nose.tools import assert_equal


    class LargeContTest(object):
        def test(self, sol):
            assert_equal(sol([1, 2, -1, 3, 4, -1]), 9)
            assert_equal(sol([1, 2, -1, 3, 4, 10, 10, -10, -1]), 29)
            assert_equal(sol([-1, 1]), 1)
            print('ALL TEST CASES PASSED')


    # Run Test
    t = LargeContTest()
    t.test(kadane_algorithm_with_bounds)
