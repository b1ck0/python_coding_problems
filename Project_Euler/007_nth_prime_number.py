# https://www.hackerrank.com/contests/projecteuler/challenges/euler007/problem

def find_primes(n):
    primes = [2]
    current = 2

    while len(primes) < n:
        remainders = [1 if current % prime == 0 else 0 for prime in primes]
        if not any(remainders):
            primes.append(current)

        current += 1

    return primes[-1]


if __name__ == "__main__":
    print(find_primes(10001))
