def finder(array1: list, array2: list) -> int:
    """
    :param array1: list
    :param array2: shuffled array1 where one element is randomly removed
    :return: the missing element
    """

    counter = dict()

    for number in array1:
        if number not in counter:
            counter[number] = 1
        else:
            counter[number] += 1

    for number in array2:
        counter[number] -= 1

    for number in counter:
        if counter[number] != 0:
            return number


def finder_xor(array1: list, array2: list) -> int:
    result = 0

    for number in array1 + array2:
        result ^= number

    return result


if __name__ == "__main__":
    from nose.tools import assert_equal


    class TestFinder(object):

        def test(self, sol):
            assert_equal(sol([0, 0, 1, 1], [0, 0, 1]), 1)
            assert_equal(sol([5, 5, 7, 7], [5, 7, 7]), 5)
            assert_equal(sol([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]), 5)
            assert_equal(sol([9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 5, 4, 3, 2, 1]), 6)
            print('ALL TEST CASES PASSED')


    # Run test
    t = TestFinder()
    t.test(finder_xor)
