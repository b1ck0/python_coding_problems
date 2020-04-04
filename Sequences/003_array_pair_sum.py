def pair_sum(array: list, s: int, test=None):
    """
    :param test: running a test case or not
    :param array: list of integers
    :param s: sum
    :return: list of unique pairs [(a1,b1), (a2,b2)] where ai+bi=s
    """
    if test is None:
        test = True

    explored_integers = []
    pair_sums = []

    for i in range(len(array)):
        if array[i] not in explored_integers:
            if s - array[i] in array[i:]:
                pair_sums.append((array[i], s - array[i]))
                explored_integers.append(array[i])
                explored_integers.append(s-array[i])
        else:
            pass

    print(pair_sums)

    if test:
        return len(pair_sums)
    else:
        return pair_sums


if __name__ == "__main__":
    from nose.tools import assert_equal


    class TestPair(object):

        def test(self, sol):
            assert_equal(sol([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1], 10), 6)
            assert_equal(sol([1, 2, 3, 1], 3), 1)
            assert_equal(sol([1, 3, 2, 2], 4), 2)
            print('ALL TEST CASES PASSED')


    # Run tests
    t = TestPair()
    t.test(pair_sum)
