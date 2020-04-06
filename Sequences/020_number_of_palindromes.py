def is_palindrome(sequence, min_length=2):
    n = len(sequence)

    if n < min_length:
        return False

    midpoint = n // 2

    for i in range(midpoint):
        if sequence[i] != sequence[n - 1 - i]:
            return False

    return True


def number_of_palindromes(string):
    """
    abba, aba, level are palindromes
    :param string:
    :return: number of palindromes in the string
    :assuming:
        - palindromes do not overlap
        - minimum length of a palindrome is 3
    """
    n = len(string)
    palindromes = dict()  # (middle: start, end)

    for i in range(1, n - 1):
        start = end = i
        while start >= 0 and end <= n:
            if is_palindrome(string[start:end]):
                palindromes[i] = string[start:end]
            if i - start == end - i:
                end += 1
            elif i - start < end - i:
                start -= 1
            else:
                end += 1

    return len(palindromes), palindromes


if __name__ == "__main__":
    print(is_palindrome('123456787654321'))
    print(is_palindrome('level'))
    print(is_palindrome('abba'))
    print(is_palindrome('kur'))
    print(number_of_palindromes('abalevelbccb'))
