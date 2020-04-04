def unique_characters(string: str) -> bool:
    seen = []

    for character in string:
        if character not in seen:
            seen.append(character)
        else:
            return False

    return True


if __name__ == "__main__":
    from nose.tools import assert_equal


    class TestUnique(object):

        def test(self, sol):
            assert_equal(sol(''), True)
            assert_equal(sol('goo'), False)
            assert_equal(sol('abcdefg'), True)
            print('ALL TEST CASES PASSED')


    # Run Tests
    t = TestUnique()
    t.test(unique_characters)
