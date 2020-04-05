def divisible_sum_pairs(array, k):
    """
    :param array: 2 <= len(array) <= 100
    :param k: 1 <= k <= 100
    :return: (a[i], a[j]), where (a[i] + a[j])%k==0
    """

    pairs = []

    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if (array[i] + array[j]) % k == 0:
                pairs.append((array[i], array[j]))

    return pairs


if __name__ == "__main__":
    print(divisible_sum_pairs([1, 3, 2, 6, 1, 2], 3))  # ---> 5
    print(divisible_sum_pairs([1, 2, 3, 4, 5, 6], 5))  # ---> 3
