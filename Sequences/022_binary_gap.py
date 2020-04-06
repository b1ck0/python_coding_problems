def binary_gap(number):
    """
    https://app.codility.com/programmers/lessons/1-iterations/binary_gap/
    :param number: integer
    :return: maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of number
    """

    def to_binary(number):
        """
        :param number: integer
        :return: return a string representation of the number
        """
        return str("{:32b}".format(number)).replace(' ', '')

    number_in_binary = to_binary(number)

    if len(number_in_binary) < 2:
        return 0

    current_gap = 0
    longest_gap = 0

    for i in range(1, len(number_in_binary)):
        if number_in_binary[i] == '0':
            current_gap += 1
        elif current_gap > 0 and number_in_binary[i] == '1':
            if longest_gap < current_gap:
                longest_gap = current_gap
            current_gap = 0

    return longest_gap


if __name__ == "__main__":
    print(binary_gap(1041))
    print(binary_gap(32))
