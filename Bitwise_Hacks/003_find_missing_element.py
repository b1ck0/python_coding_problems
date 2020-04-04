def find_missing_element(array1, array2):
    result = 0

    for number in array1 + array2:
        result ^= number

    return result


if __name__ == "__main__":
    from nose.tools import assert_equal


    class TestClass(object):

        def test(self, sol):
            assert_equal(sol([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 6, 7, 8, 9, 10]), 5)
            print('ALL TEST CASES PASSED')


    # Run Tests
    t = TestClass()
    t.test(find_missing_element)
