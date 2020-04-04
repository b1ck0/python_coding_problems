def haker_rank_wraper(n, k):
    """
    haker_rank_wraper(9875, 1)
    super_digit(9875)   9+8+7+5 = 29
    super_digit(29) 	2 + 9 = 11
    super_digit(11)		1 + 1 = 2
    super_digit(2)		= 2
    """

    def sum_digits(number):
        if number < 10:
            return number
        else:
            return number % 10 + sum_digits(number // 10)

    def super_digit(number):
        if number < 10:
            return number
        else:
            return super_digit(sum_digits(number))

    p = int(str(n) * k)
    return super_digit(p)


if __name__ == "__main__":
    print(haker_rank_wraper(148, 3))
