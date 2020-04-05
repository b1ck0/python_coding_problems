def equalize_array(array):
    freqs = dict()

    for i in range(len(array)):
        if array[i] not in freqs:
            freqs[array[i]] = 1
        else:
            freqs[array[i]] += 1

    sorted_freqs = sorted(freqs.items(), key=lambda x: x[1], reverse=True)

    return len(array) - sorted_freqs[0][1]


if __name__ == "__main__":
    print(equalize_array([3, 3, 2, 1, 3]))
