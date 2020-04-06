def tape_equilibrium(array):
    # https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/
    # write your code in Python 3.6
    n = len(array)

    s = {
        0: array[0],
        n: sum(array)
    }

    d_min = float('Inf')

    for i in range(1, n):
        s[i] = s[i - 1] + array[i]
        right_sum = s[n] - s[i - 1]
        diff = abs(right_sum - s[i - 1])
        if d_min > diff:
            d_min = diff

    return d_min


if __name__ == "__main__":
    tape_equilibrium([3, 1, 2, 4, 3])
    print("=" * 50)
    print(tape_equilibrium([1, 1]))  # expected 0
    print(tape_equilibrium([1, 2]))  # expected 1
