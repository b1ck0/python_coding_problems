def nth_fibonacci(n: int) -> int:
    sequence = [0, 1]

    for i in range(2, n):
        sequence.append(sequence[i - 2] + sequence[i - 1])

    return sequence[n-1]


if __name__ == "__main__":
    from nose.tools import assert_equal


    class TestClass(object):

        def test(self, sol):
            assert_equal(sol(2), 1)
            assert_equal(sol(6), 5)
            print('ALL TEST CASES PASSED')


    # Run Tests
    t = TestClass()
    t.test(nth_fibonacci)
