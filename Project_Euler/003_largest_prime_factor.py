# https://www.hackerrank.com/contests/projecteuler/challenges/euler003/problem

def factorize(number, factors=None):
    if factors is None:
        factors = []

    if number == 1:
        factors.append(number)
    elif number in factors:
        factors.append(number)
    else:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                factors.append(i)
                return factorize(number // i, factors)

        else:
            factors.append(number)

    return factors


def largest_prime_factors(n):
    factors = factorize(n)

    return max(factors)


if __name__ == "__main__":
    print(largest_prime_factors(10))
    print(largest_prime_factors(17))
    print(largest_prime_factors(600851475143))
