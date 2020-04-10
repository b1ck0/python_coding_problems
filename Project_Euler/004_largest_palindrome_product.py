# https://www.hackerrank.com/contests/projecteuler/challenges/euler004/problem

def digitize(n):
    if n < 10:
        return [n]
    else:
        return [n % 10] + digitize(n // 10)


def is_palindrome(n, digits=None):
    if digits is None:
        digits = digitize(n)

    if len(digits) <= 1:
        return True
    else:
        if digits[0] != digits[-1]:
            return False
        else:
            return is_palindrome(n, digits[1:-1])


def find_palindromic_numbers(n_min, n_max, k_max):
    for i in range(n_max - 1, n_min - 1, -1):
        if is_palindrome(i):
            for j in range(999, 99, -1):
                if i % j == 0 and i // j < k_max:
                    return i, j, i // j


if __name__ == "__main__":
    print(digitize(123213))
    print(digitize(793397))
    print(is_palindrome(12321))
    print(is_palindrome(123211))
    print(is_palindrome(101101))
    print(find_palindromic_numbers(143 * 707, 999 * 999, 1000))
    print(find_palindromic_numbers(143 * 707, 101110, 1000))
    print(find_palindromic_numbers(143 * 707, 800000, 1000))
