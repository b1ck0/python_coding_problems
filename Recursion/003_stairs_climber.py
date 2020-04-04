def num_climbs(level, cache=None):
    """
    the climber can take only 1 or 2 stair jump at each step
    :param level: level to reach
    :param cache: memoization block
    :return: number of ways to get to the desired level
    """
    if cache is None:
        cache = {
            1: 1,
            2: 2
        }

    if level in cache:
        return cache[level]
    else:
        cache[level] = num_climbs(level - 1) + num_climbs(level - 2)
        return cache[level]


if __name__ == "__main__":
    from nose.tools import assert_equal


    class TestClass(object):

        def test(self, sol):
            assert_equal(sol(1), 1)
            assert_equal(sol(2), 2)
            assert_equal(sol(3), 3)
            assert_equal(sol(4), 5)
            print('ALL TEST CASES PASSED')


    # Run Tests
    t = TestClass()
    t.test(num_climbs)
