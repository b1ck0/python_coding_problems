def anagram(str_1: str, str_2: str) -> bool:
    """
    :param str_1: word 1
    :param str_2: word 2
    :return: True if str_1 and str_2 are anagrams, False otherwise
    - two strings are anagrams of they all contain the same letters
    - ignore all spaces and caps
    """
    str_1, str_2 = map(lambda x: x.lower().replace(' ', ''), [str_1, str_2])

    # probably the fastest solution would be
    # if sorted(str_1) == sorted(str_2):
    #     return True

    if len(str_1) != len(str_2):
        return False

    letter_dict = dict()

    for letter in str_1:
        if letter not in letter_dict.keys():
            letter_dict[letter] = 1
        else:
            letter_dict[letter] += 1

    for letter in str_2:
        if letter not in letter_dict.keys():
            letter_dict[letter] = 1
        else:
            letter_dict[letter] -= 1

    for letter in letter_dict.keys():
        if letter_dict[letter] != 0:
            return False

    return True


if __name__ == "__main__":
    from nose.tools import assert_equal


    class AnagramTest(object):

        def test(self, sol):
            assert_equal(sol('go go go', 'gggooo'), True)
            assert_equal(sol('abc', 'cba'), True)
            assert_equal(sol('hi man', 'hi     man'), True)
            assert_equal(sol('aabbcc', 'aabbc'), False)
            assert_equal(sol('aabbcc', 'aabbbc'), False)
            assert_equal(sol('123', '1 2'), False)
            print('ALL TEST CASES PASSED')


    # Run Tests
    t = AnagramTest()
    t.test(anagram)
