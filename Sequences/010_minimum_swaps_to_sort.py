def minimum_swaps(array: list) -> int:
    value_map = [(array[index], index + 1) for index in range(len(array))]
    misplaced_values = list(filter(lambda x: x[0] != x[1], value_map))
    misplaced_values = list(map(lambda x: (x[0], x[1], x[0] - x[1]), misplaced_values))

    if len(misplaced_values) == 0:
        return 0
    elif len(misplaced_values) % 2 == 0:
        return len(misplaced_values) - 1
    else:
        return len(misplaced_values) - 2


if __name__ == "__main__":
    from nose.tools import assert_equal


    class TestClass(object):

        def test(self, sol):
            assert_equal(sol([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 0)
            assert_equal(sol([7, 1, 3, 2, 4, 5, 6]), 5)
            assert_equal(sol([1, 3, 5, 2, 4, 6, 7]), 3)
            assert_equal(sol([2, 3, 4, 1, 5]), 3)
            assert_equal(sol([4, 3, 1, 2, ]), 3)
            print('ALL TEST CASES PASSED')


    # Run Tests
    t = TestClass()
    t.test(minimum_swaps)
