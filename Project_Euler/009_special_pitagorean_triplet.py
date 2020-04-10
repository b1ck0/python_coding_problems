# https://www.hackerrank.com/contests/projecteuler/challenges/euler009/problem

def triplet(n):
    upper_bound_a = ((n - 3) // 3) + 1
    candidates = []

    for a in range(3, upper_bound_a):
        b = n * (2 * a - n) / (2 * (a - n))  # a**2 + b**2 = (n-a-b)**2
        c = n - a - b  # a+b+c=n
        if b == int(b) and c == int(c):
            if a ** 2 + b ** 2 == c ** 2:
                candidates.append(a * b * c)
                print(a, b, c, a + b + c, a * b * c)
        else:
            continue

    if len(candidates):
        return int(max(candidates))
    else:
        return -1


if __name__ == "__main__":
    print(triplet(3000))
