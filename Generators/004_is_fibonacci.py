def is_fibonacci(number):
    """
    https://www.hackerrank.com/challenges/is-fibo/problem
    :param number: number
    :return: true if number in fibonacci sequence else otherwise
    """

    def fibonacci():
        current, previous = 0, 1
        while True:
            yield current
            current, previous = current + previous, current

    generator = fibonacci()

    for i in range(number + 2):
        fib_n = next(generator)

        if fib_n > number:
            return False

        if fib_n == number:
            return True


if __name__ == "__main__":
    print(is_fibonacci(5))  # --> true
    print(is_fibonacci(7))  # --> false
    print(is_fibonacci(8))  # --> true
    print(is_fibonacci(8021922698))  # --> false
    print(is_fibonacci(5496312114))  # --> false
    print(is_fibonacci(7007806610))  # --> false
    print(is_fibonacci(7312352899))  # --> false
    print(is_fibonacci(1))  # --> true
    print(is_fibonacci(3))  # --> true
