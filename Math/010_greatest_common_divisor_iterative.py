def greatest_common_divisor(a, b):
    candidate = min(a, b)

    while a % candidate != 0 or b % candidate != 0:
        candidate -= 1

    return candidate


if __name__ == "__main__":
    from nose.tools import assert_equal


class TestClass(object):

    def test(self, sol):
        assert_equal(sol(38, 18), 2)
        assert_equal(sol(49, 63), 7)
        assert_equal(sol(114, 228), 114)
        assert_equal(sol(285, 105), 15)
        assert_equal(sol(300, 75), 75)
        assert_equal(sol(168, 168), 168)
        assert_equal(sol(216, 288), 72)
        assert_equal(sol(273, 182), 91)
        assert_equal(sol(4, 92), 4)
        assert_equal(sol(4, 36), 4)
        print('ALL TEST CASES PASSED')


# Run Tests
t = TestClass()
t.test(greatest_common_divisor)
