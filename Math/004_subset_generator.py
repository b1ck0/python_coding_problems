def generate_all_subsets(array):
    n = len(array)

    for i in range(2 ** n):
        subsets = []

        for j in range(n):
            if (i >> j) & 1 != 0:  # if (i // 2**j) % 2 == 1
                subsets.append(array[j])

        yield subsets


if __name__ == "__main__":

    iterator = generate_all_subsets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    for _ in range(10):
        print(next(iterator))
