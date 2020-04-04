def power_sum(number, exp, current=1):
    """
    https://www.hackerrank.com/challenges/the-power-sum/problem
    :param number: 1 <= number <= 1000
    :param exp: 2 <= exp <= 10
    :return: number of possible combinations of unique numbers where sum(k^exp) = number
    """

    power = current ** exp

    # edge-case
    if power > number:
        return 0
    elif power == number:
        return 1
    else:
        return power_sum(number, exp, current + 1) + power_sum(number - power, exp, current + 1)


if __name__ == "__main__":
    print(power_sum(100, 2))
    print(power_sum(1000, 3))
