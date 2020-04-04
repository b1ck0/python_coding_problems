import math


def radiation_exposure(start, stop, step, f):
    if stop - start < 0.01:
        return 0
    else:
        return f(start) * step + radiation_exposure(start + step, stop, step, f)


if __name__ == "__main__":
    from nose.tools import assert_equal


class TestClass(object):

    def test(self, sol):
        def f(x):
            return 10 * math.e ** (math.log(0.5) / 5.27 * x)

        assert_equal(round(sol(0, 5, 1, f), 2), round(39.10318784326239, 2))
        assert_equal(round(sol(5, 11, 1, f), 2), round(22.94241041057671, 2))
        assert_equal(round(sol(0, 11, 1, f), 2), round(62.0455982538, 2))

        def f(x):
            return 400 * math.e ** (math.log(0.5) / 3.66 * x)

        assert_equal(round(sol(0, 4, 0.25, f), 2), round(1148.6783342153556, 2))
        assert_equal(round(sol(5, 10, 0.25, f), 2), round(513.4662018628549, 2))

        def f(x):
            return 200 * math.e ** (math.log(0.5) / 14.1 * x)

        assert_equal(round(sol(0, 3, 0.1, f), 2), round(559.2259707824549, 2))
        assert_equal(round(sol(14, 20, 0.1, f), 2), round(523.4527522388149, 2))
        assert_equal(round(sol(48, 72, 0.4, f), 2), round(268.79947333082856, 2))
        assert_equal(round(sol(72, 96, 0.4, f), 2), round(82.61081970598813, 2))

        def f(x):
            return 150 * math.e ** (math.log(0.5) / 32.2 * x)

        assert_equal(round(sol(0, 40, 1, f), 2), round(4066.0849302266774, 2))
        assert_equal(round(sol(100, 400, 4, f), 2), round(843.5828023451531, 2))
        assert_equal(round(sol(1000, 4000, 15, f), 2), round(3.6525375905841067e-06, 2))

        def f(x):
            return 60 * math.e ** (math.log(0.5) / 55.6 * x)

        assert_equal(round(sol(0, 60, 0.5, f), 2), round(2542.768831286683, 2))
        assert_equal(round(sol(60, 120, 0.5, f), 2), round(1203.5229215597114, 2))
        assert_equal(round(sol(600, 1200, 5, f), 2), round(2.799597134148232, 2))

        print('ALL TEST CASES PASSED')


# Run Tests
t = TestClass()
t.test(radiation_exposure)
