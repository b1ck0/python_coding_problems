def is_palindrome(sequence):
    n = len(sequence)
    midpoint = n // 2

    for i in range(midpoint):
        if sequence[i] != sequence[n - 1 - i]:
            return False

    return True


if __name__ == "__main__":
    from nose.tools import assert_equal


    class TestClass(object):

        def test(self, sol):
            assert_equal(sol([1, 2, 3, 4, 5, 6]), False)
            assert_equal(sol([1, 2, 3, 2, 1]), True)
            assert_equal(sol([1, 2, 3, 4, 3, 2, 1]), True)
            assert_equal(sol([1, 1, 1, 1]), True)
            assert_equal(sol([1, 2, 2, 1]), True)
            print('ALL TEST CASES PASSED')


    # Run Tests
    t = TestClass()
    t.test(is_palindrome)
