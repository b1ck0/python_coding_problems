def remove_duplicates(sorted_array):
    # https://leetcode.com/problems/remove-duplicates-from-sorted-array/

    seen = dict()

    for i, element in enumerate(sorted_array):
        seen[element] = seen.get(element, 0) + 1

    return len(seen)


if __name__ == "__main__":
    print(remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
    print(remove_duplicates([1,1,2]))
