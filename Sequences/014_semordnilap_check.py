def are_semordnilap(a, b, depth=None):
    if len(a) != len(b):
        return False

    if a == b and depth is not None:
        return True

    if depth is None:
        if a == b:
            return False
        else:
            depth = 1

    if a[0] == b[-1]:
        return are_semordnilap(a[1:], b[:-1], depth + 1)
    else:
        return False


if __name__ == "__main__":
    from nose.tools import assert_equal


    class TestClass(object):

        def test(self, sol):
            assert_equal(sol('live', 'evil'), True)
            assert_equal(sol('tact', 'cat'), False)
            assert_equal(sol('desserts', 'stressed'), True)
            assert_equal(sol('level', 'level'), False)
            assert_equal(sol('semordnilap', 'palindrome'), False)
            assert_equal(sol('rats live on', 'no evil star'), True)
            assert_equal(sol('psmrinhtxedqf', 'vamhkelo'), False)
            assert_equal(sol('bowxnjsgqval', 'nzfrjpwsbdlt'), False)
            assert_equal(sol('bzedaqvfrtugmc', 'ohbjgrqxvtm'), False)
            assert_equal(sol('e', 'x'), False)
            assert_equal(sol('e', 'e'), False)
            print('ALL TEST CASES PASSED')


    # Run Tests
    t = TestClass()
    t.test(are_semordnilap)
