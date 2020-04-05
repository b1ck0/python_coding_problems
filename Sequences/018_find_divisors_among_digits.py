def find_divisors(number):
    """
    https://www.hackerrank.com/challenges/find-digits/problem
    :param number:
    :return:
    """

    def find_digits(number):
        if number < 10:
            return [number]
        else:
            return [number % 10] + find_digits(number // 10)

    digits = find_digits(number)
    divisors = [digit for digit in digits if (digit != 0) and (number % digit == 0)]

    return divisors


if __name__ == "__main__":
    print(find_divisors(12))
    print(find_divisors(1012))
