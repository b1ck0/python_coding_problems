# https://www.hackerrank.com/contests/projecteuler/challenges/euler002/problem

def fibonacci(limit):
    sequence = [1, 2]

    while sequence[-1] < limit:
        sequence.append(sequence[-2] + sequence[-1])

    return sum([i for i in sequence if i < limit and i % 2 == 0])


if __name__ == "__main__":
    print(fibonacci(4_000_000))
