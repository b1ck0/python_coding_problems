# A - list of integers [-1_000_000; 1_000_000]
# N - integer within [1;100_000]

def solution(A):
    # Given an array A of N integers, returns the smallest positive integer
    # (greater than 0) that does not occur in A
    # A = [1,3,6,4,1,2] -> 5
    # A = [1,2,3] -> 4
    # A = [-1,-3] -> 1

    positives = [e for e in A if e > 0]

    for i in range(1, 1_000_000 + 1):
        if i not in positives:
            return i
