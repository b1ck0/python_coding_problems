def horners_algorithm(a: list, x: int) -> int:
    """
    :return: y = dot(A, [1, x, x^2, x^3, ... x^n])
    """

    b = a[-1]

    for i in range(len(a) - 2, -1, -1):
        b = b * x + a[i]

    return b


if __name__ == "__main__":
    from nose.tools import assert_equal


    class TestClass(object):

        def test(self, sol):
            assert_equal(sol([1, 1, 1, 1, 1, 1], 1), 6)
            assert_equal(sol([1, 1, 1, 1, 1, 1], 0), 1)
            assert_equal(sol([1, 2, 3, 4, 5, 6], 1), 21)
            assert_equal(sol([1, 1, 1, 1, 1, 1], 2), 1 + 2 + 2 ** 2 + 2 ** 3 + 2 ** 4 + 2 ** 5)
            print('ALL TEST CASES PASSED')


    # Run Tests
    t = TestClass()
    t.test(horners_algorithm)
