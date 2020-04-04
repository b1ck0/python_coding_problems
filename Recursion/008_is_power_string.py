def is_power_string(phrase: str, list_of_words: list, output=None) -> list:
    if output is None:
        output = []

    for word in list_of_words:
        if phrase.startswith(word):
            output.append(word)

            return is_power_string(phrase[len(word):], list_of_words, output)

    return output


if __name__ == "__main__":
    from nose.tools import assert_equal


    class TestReverse(object):

        def test_rev(self, solution):
            assert_equal(solution('themanran', ['the', 'ran', 'man']), ['the', 'ran', 'man'])
            assert_equal(solution('ilovedogsJohn', ['i', 'am', 'a', 'dogs', 'lover', 'love', 'John']),
                         ['i', 'love', 'dogs', 'John'])
            assert_equal(solution('themanran', ['clown', 'ran', 'man']), [])
            print('PASSED ALL TEST CASES!')


    # Run Tests
    test = TestReverse()
    test.test_rev(is_power_string)
