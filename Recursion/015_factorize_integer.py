def factorize(number, factors=None):
    if factors is None:
        factors = []

    if number == 1:
        factors.append(number)
    else:
        for i in range(2, number + 1):
            if number % i == 0:
                factors.append(i)
                return factorize(number // i, factors)

    return sorted(factors)


if __name__ == "__main__":
    print(factorize(1))
    print(factorize(2))
    print(factorize(3))
    print(factorize(10))
    print(factorize(25))
