def isBalanced(s):
    reverse = {
        "]": "[",
        ")": "(",
        "}": "{"
    }

    if s[0] in reverse:
        return False

    stack = []
    for char in s:
        if char not in reverse:
            stack.append(char)
        else:
            if not len(stack):
                return False
            last = stack.pop()
            if reverse[char] != last:
                return False

    if not len(stack):
        return True
    else:
        return False
