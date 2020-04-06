def merge_sort(array):
    if len(array) > 1:
        i = len(array) // 2
        left = array[:i]
        right = array[i:]

        merge_sort(left)  # sort left half
        merge_sort(right)  # sort right half

        i, j, k = 0, 0, 0

        # if both lists have the same length this will be the only while block executed
        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1

            k += 1

        # this will be executed of len(left) > len(right)
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        # this will be executed of len(right) > len(left)
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

    return array


if __name__ == "__main__":
    print(merge_sort([1, 33, 4, 6, 2, 3, 56, 67, 7, 43, 2, 2, 1, 23, 5, 6, 7, 4, 3, 2, 2, 3, 5, 6, 123]))
