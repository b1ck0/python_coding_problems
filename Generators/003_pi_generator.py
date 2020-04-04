def odd_number_generator():
    n = 1
    while True:
        yield n
        n += 2


def pi_generator():
    """
    https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80
    :return:
    """
    odd_numbers = odd_number_generator()
    approximated_pi = 0
    while True:
        # we have two yields here as this is a alternating sequence
        # no problem to remove the first yield but then one cycle of the generator
        # would actually be two cycles for i so ...
        # in addition there is no better way of keeping track of the +- thing (think!)
        approximated_pi += (4 / next(odd_numbers))
        yield approximated_pi
        approximated_pi -= (4 / next(odd_numbers))
        yield approximated_pi


if __name__ == "__main__":
    pi_approximation = pi_generator()

    for i in range(1000000):
        print(f"step = {i}, current pi approximation = {next(pi_approximation)}")
