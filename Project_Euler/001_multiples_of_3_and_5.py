# https://www.hackerrank.com/contests/projecteuler/challenges/euler001/problem

def sum_up_to(n):
    return n * (n - 1) >> 1


def multiples_3(n):
    k_3 = (n - 1) // 3
    k_5 = (n - 1) // 5
    k_15 = (n - 1) // 15

    sum_3 = sum_up_to(k_3 + 1)
    sum_5 = sum_up_to(k_5 + 1)
    sum_15 = sum_up_to(k_15 + 1)

    return int(3 * sum_3 + 5 * sum_5 - 15 * sum_15)


if __name__ == "__main__":
    print(multiples_3(1000))
