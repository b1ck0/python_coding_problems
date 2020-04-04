def string_compression(string):

    if len(string) == 0:
        return ''

    current_char = string[0]
    current_length = 1
    compressed_string = ''

    for i in range(1, len(string)):
        if string[i - 1] == string[i]:
            current_length += 1
        else:
            compressed_string += f'{current_char}{current_length}'
            current_char = string[i]
            current_length = 1

    compressed_string += f'{current_char}{current_length}'

    print(f"{string} ---> {compressed_string}")

    return compressed_string


if __name__ == "__main__":
    from nose.tools import assert_equal


    class TestCompress(object):

        def test(self, sol):
            assert_equal(sol(''), '')
            assert_equal(sol('AABBCC'), 'A2B2C2')
            assert_equal(sol('AAABCCDDDDD'), 'A3B1C2D5')
            print('ALL TEST CASES PASSED')


    # Run Tests
    t = TestCompress()
    t.test(string_compression)
