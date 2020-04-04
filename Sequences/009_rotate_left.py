def rotate_left(array: list, n_rotations: int) -> list:
    """
    https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
    :param array: some array
    :param n_rotations: number of shifts to left
    :return: shifted array
    """
    right = array[n_rotations:]
    left = array[:n_rotations]

    return right + left


if __name__ == "__main__":
    from nose.tools import assert_equal


    class TestClass(object):

        def test(self, sol):
            assert_equal(sol([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1), [2, 3, 4, 5, 6, 7, 8, 9, 10, 1])
            assert_equal(sol([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2), [3, 4, 5, 6, 7, 8, 9, 10, 1, 2])
            assert_equal(sol([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3), [4, 5, 6, 7, 8, 9, 10, 1, 2, 3])
            assert_equal(sol([41, 73, 89, 7, 10, 1, 59, 58, 84, 77, 77, 97, 58, 1, 86, 58, 26, 10, 86, 51], 10),
                         [77, 97, 58, 1, 86, 58, 26, 10, 86, 51, 41, 73, 89, 7, 10, 1, 59, 58, 84, 77])
            print('ALL TEST CASES PASSED')


    # Run Tests
    t = TestClass()
    t.test(rotate_left)
