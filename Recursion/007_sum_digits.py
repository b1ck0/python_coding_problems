def sum_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_digits(n // 10)


if __name__ == "__main__":
    from nose.tools import assert_equal


    class TestReverse(object):

        def test_rev(self, solution):
            assert_equal(solution(4), 4)
            assert_equal(solution(41), 5)
            assert_equal(solution(1111111111), 10)
            print('PASSED ALL TEST CASES!')


    # Run Tests
    test = TestReverse()
    test.test_rev(sum_digits)
