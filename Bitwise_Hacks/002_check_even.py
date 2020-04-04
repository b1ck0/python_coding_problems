def is_even(number):
    if number & 1 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    from nose.tools import assert_equal


    class TestClass(object):

        def test(self, sol):
            assert_equal(sol(2), True)
            assert_equal(sol(3), False)
            print('ALL TEST CASES PASSED')


    # Run Tests
    t = TestClass()
    t.test(is_even)
