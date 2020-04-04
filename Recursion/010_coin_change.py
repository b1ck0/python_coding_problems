def coin_change(amount: int, coins: list, output=None):
    """
    :param amount: change
    :param coins: set of coins
    :return: MIN [ len(coins) ] which add up to amount
    """
    if output is None:
        output = []

    # base case
    if amount == 0:
        print(output)
        return len(output)

    if amount >= coins[-1]:
        output.append(coins[-1])
        return coin_change(amount - coins[-1], coins, output)
    else:
        return coin_change(amount, coins[:-1], output)


if __name__ == "__main__":
    from nose.tools import assert_equal


    class TestCoins(object):

        def check(self, solution):
            coins = [1, 5, 10, 25]
            assert_equal(solution(45, coins), 3)
            assert_equal(solution(23, coins), 5)
            assert_equal(solution(74, coins), 8)
            print('Passed all tests.')


    # Run Test

    test = TestCoins()
    test.check(coin_change)
