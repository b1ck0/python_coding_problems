def check_parentheses(string: str) -> bool:
    """
    :param string: string of parentheses [, (, {, }, ), ] without any other characters/spaces whatsoever
    :return: all parentheses are closed
    """
    opening_parentheses = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    parentheses_stack = []

    for char in string:
        if char in ['[', '(', '{']:
            parentheses_stack.append(char)
        else:
            if parentheses_stack.pop() != opening_parentheses[char]:
                return False

    return True


if __name__ == "__main__":
    from nose.tools import assert_equal


    class TestClass(object):

        def test(self, sol):
            assert_equal(sol('()'), True)
            assert_equal(sol('([])'), True)
            assert_equal(sol('([{}])'), True)
            assert_equal(sol('()()()()()()()()'), True)
            assert_equal(sol('([)])'), False)
            print('ALL TEST CASES PASSED')


    # Run Tests
    t = TestClass()
    t.test(check_parentheses)
