def largest_range(array):
    best_range = []
    longest_length = 0
    explored = {value: False for value in array}

    for number in array:
        if explored[number]:
            continue
        else:
            explored[number] = True
            current_length = 1
            left = number - 1
            right = number + 1
            while left in explored:
                explored[left] = True
                current_length += 1
                left -= 1
            while right in explored:
                explored[right] = True
                current_length += 1
                right += 1

            if current_length > longest_length:
                longest_length = current_length
                best_range = [left + 1, right - 1]

    return best_range


if __name__ == "__main__":
    from nose.tools import assert_equal


    class TestClass(object):

        def test(self, sol):
            assert_equal(sol([8, 4, 2, 10, 3, 6, 7, 9, 1]), [6, 10])
            assert_equal(sol([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]), [0, 7])
            print('ALL TEST CASES PASSED')


    # Run Tests
    t = TestClass()
    t.test(largest_range)
