# https://www.hackerrank.com/contests/projecteuler/challenges/euler010/problem

def sieve_of_eratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:

        if prime[p]:
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1

    prime[0] = False
    prime[1] = False

    return [i for i in range(n + 1) if prime[i]]


if __name__ == "__main__":
    print(sum(sieve_of_eratosthenes(5)))
    print(sum(sieve_of_eratosthenes(10)))
    print(sum(sieve_of_eratosthenes(2_000_000)))
