# https://www.hackerrank.com/contests/projecteuler/challenges/euler005/problem
import functools


def find_primes(n):
    primes = [1, 2]
    array = list(range(1, n + 1))

    while len(array):
        if array[0] not in primes:
            primes.append(array[0])

        array = [i for i in array if (i % primes[-1] != 0) and (i not in primes)]

    return primes


def extract_powers(primes, number, powers=None):
    if powers is None:
        powers = dict()

    for prime in [i for i in primes if i <= number]:
        power = 2

        if prime ** power > number:
            continue
        elif prime ** power == number:
            if prime not in powers:
                powers[prime] = power
            else:
                powers[prime] = max(powers[prime], power)
        else:
            while prime ** power <= number:
                if prime ** power == number:
                    if prime not in powers:
                        powers[prime] = power
                    else:
                        powers[prime] = max(powers[prime], power)

                power += 1


def find_smalles_multiple(n):
    if n == 1:
        return 1

    primes = find_primes(n)
    multiples = [i for i in range(1, n + 1) if i not in primes]
    powers = dict()

    for multiple in multiples:
        extract_powers(primes[1:], multiple, powers)

    for prime in powers:
        primes.append(prime ** (powers[prime] - 1))

    return functools.reduce(lambda a, b: a * b, primes)


if __name__ == "__main__":
    print(find_smalles_multiple(10))
    print(find_smalles_multiple(20))
