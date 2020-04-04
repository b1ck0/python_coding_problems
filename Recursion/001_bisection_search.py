def search(element, array: list):
    """
    :param element: some element
    :param array: sorted list
    :return: element in list
    """
    if len(array) == 0 or element == '' or element is None:
        return False

    if len(array) == 1:
        return element == array[0]

    n = len(array)
    mid = n // 2

    if element == array[mid]:
        return True
    elif element < array[mid]:
        return search(element, array[:mid])
    else:
        return search(element, array[mid:])


if __name__ == "__main__":
    from nose.tools import assert_equal


class TestClass(object):

    def test(self, sol):
        assert_equal(sol('a', ''), False)
        assert_equal(sol('u', 'llmrtwy'), False)
        assert_equal(sol('e', 'ceeijlpvv'), True)
        assert_equal(sol('w', 'aehirww'), True)
        assert_equal(sol('d', 'cdfgiiilnpprvwxxzz'), True)
        assert_equal(sol('g', 'bdefffgklmooqrwx'), True)
        assert_equal(sol('f', 'cefgijlmoorrtttxyy'), True)
        assert_equal(sol('u', 'lmosstuuvv'), True)
        assert_equal(sol('x', 'bcddefghijnppqruy'), False)
        assert_equal(sol('p', 'acddeghkkpqsuxy'), True)
        assert_equal(sol(5, [1, 2, 3, 4, 5, 6]), True)
        assert_equal(sol(10, [1, 2, 3, 4, 5, 6]), False)
        print('ALL TEST CASES PASSED')


# Run Tests
t = TestClass()
t.test(search)
