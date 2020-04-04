def string_permutations(string: str) -> list:
    # string_permutations('abc') = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    output = []

    if len(string) == 1:
        return [string]
    else:
        for position, letter in enumerate(string):
            for permutation in string_permutations(string[:position] + string[position + 1:]):
                output += [letter + permutation]

    return output


if __name__ == "__main__":
    from nose.tools import assert_equal


    class TestPerm(object):

        def test(self, solution):
            assert_equal(sorted(solution('abc')), sorted(['abc', 'acb', 'bac', 'bca', 'cab', 'cba']))
            assert_equal(sorted(solution('dog')), sorted(['dog', 'dgo', 'odg', 'ogd', 'gdo', 'god']))

            print('All test cases passed.')


    # Run Tests
    t = TestPerm()
    t.test(string_permutations)
