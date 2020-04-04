def swap_xor(a, b):
    # [x xor x = 0] and [0 xor x = x]
    a = a ^ b
    b = b ^ a
    a = a ^ b

    return a, b


if __name__ == "__main__":
    from nose.tools import assert_equal


    class TestClass(object):

        def test(self, sol):
            assert_equal(sol(1, 2), (2, 1))
            assert_equal(sol(22, 31), (31, 22))
            print('ALL TEST CASES PASSED')


    # Run Tests
    t = TestClass()
    t.test(swap_xor)
