def sentence_reversal(sentence: str) -> str:
    words = sentence.split(' ')
    words = list(filter(lambda x: x != '', words))
    words_backwards = [words[i] for i in range(len(words) - 1, -1, -1)]

    print(f"{words} -> {words_backwards}")

    return ' '.join(words_backwards)


if __name__ == "__main__":
    from nose.tools import assert_equal


    class ReversalTest(object):

        def test(self, sol):
            assert_equal(sol('    space before'), 'before space')
            assert_equal(sol('space after     '), 'after space')
            assert_equal(sol('   Hello John    how are you   '), 'you are how John Hello')
            assert_equal(sol('1'), '1')
            print("ALL TEST CASES PASSED")


    # Run and test
    t = ReversalTest()
    t.test(sentence_reversal)
