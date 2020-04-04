def power(base: float, exp: int) -> float:
    if exp == 0:
        return 1
    elif exp % 2 == 0:
        return power(base * base, exp // 2)

    return base * power(base, exp-1)


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
