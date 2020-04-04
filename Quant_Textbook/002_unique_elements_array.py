def find_unique_elements(array):
    unique_elements = []

    for number in array:
        if number in unique_elements:
            continue
        else:
            unique_elements.append(number)

    return unique_elements


def find_unique_elements_without_in(array):
    unique_elements = [array[0]]

    for i in range(1, len(array)):
        if array[i] != array[i - 1]:
            unique_elements.append(array[i])

    return unique_elements


if __name__ == "__main__":
    from nose.tools import assert_equal


    class TestClass(object):

        def test(self, sol):
            assert_equal(sol([1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]), [1, 2, 3, 4, 5, 6])
            print('ALL TEST CASES PASSED')


    # Run Tests
    t = TestClass()
    t.test(find_unique_elements)
    t.test(find_unique_elements_without_in)
