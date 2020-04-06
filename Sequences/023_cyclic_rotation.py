def solution(A, K):
    # https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/
    # write your code in Python 3.6

    N = len(A)

    if N == 0:
        return []

    if K == 0:
        return A

    return A[-K % N:] + A[:-K % N]
