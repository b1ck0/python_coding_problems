def largest_rectangle(array):
    # https://www.hackerrank.com/challenges/largest-rectangle/problem

    stack = [(0, array[0])]

    for index, value in enumerate(array):
        if value > stack[-1][1]:
            stack.append((index, value))
        else:
            while stack[-1][1] > value and len(stack):
                stack.pop()

            stack.append((index, value))

    return stack


if __name__ == "__main__":
    print(largest_rectangle([1, 2, 3, 4, 5, 6, 5, 4]))
