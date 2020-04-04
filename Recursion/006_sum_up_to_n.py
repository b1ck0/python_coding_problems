def sum_up_to_n(n, cache=None):
    if cache is None:
        cache = dict()

    if n == 1:
        return 1

    if n in cache:
        return cache[n]
    else:
        result = sum_up_to_n(n - 1) + n
        return result


if __name__ == "__main__":
    from nose.tools import assert_equal


    class TestReverse(object):

        def test_rev(self, solution):
            assert_equal(solution(4), 10)
            print('PASSED ALL TEST CASES!')


    # Run Tests
    test = TestReverse()
    test.test_rev(sum_up_to_n)
