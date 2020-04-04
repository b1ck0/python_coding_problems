def power(base: float, exp: int) -> int:
    if exp == 0:
        return 1

    result = 1

    for i in range(exp):
        result *= base

    return result


if __name__ == "__main__":
    from nose.tools import assert_equal


    class TestClass(object):

        def test(self, sol):
            assert_equal(sol(2, 1), 2)
            assert_equal(sol(2, 2), 4)
            assert_equal(sol(2, 3), 8)
            print('ALL TEST CASES PASSED')


    # Run Tests
    t = TestClass()
    t.test(power)
