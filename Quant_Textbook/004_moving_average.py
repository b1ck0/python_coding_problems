def moving_average(a: list, n: int) -> list:
    """
    :param a: array of numbers
    :param n: window of the moving average
    :return: the moving average sequence
    """
    moving_sum = sum(a[:n])
    moving_averages = [moving_sum/n]

    for i in range(n, len(a)):
        moving_sum += a[i] - a[i - n]
        moving_averages.append(moving_sum / n)

    return moving_averages


if __name__ == "__main__":
    from nose.tools import assert_equal


    class TestClass(object):

        def test(self, sol):
            assert_equal(sol([1, 1, 1, 1, 1, 1], 2), [1, 1, 1, 1, 1])
            assert_equal(sol([1, -1, 1, -1, 1, -1], 2), [0, 0, 0, 0, 0])
            print('ALL TEST CASES PASSED')


    # Run Tests
    t = TestClass()
    t.test(moving_average)
