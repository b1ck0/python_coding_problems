def coin_change(amount: int, coins: list, output=None):
    """
    :param amount:
    :param coins: denominations
    :return: # ways to give the change back
    """
    min_coins = amount

    # Check to see if we have a single coin match (BASE CASE)
    if amount in coins:
        return 1

    else:

        # for every coin value that is <= than target
        for i in [c for c in coins if c <= amount]:

            # Recursive Call (add a count coin and subtract from the target)
            num_coins = 1 + coin_change(amount - i, coins)

            # Reset Minimum if we have a new minimum
            if num_coins < min_coins:
                min_coins = num_coins

    return min_coins


if __name__ == "__main__":
    print(coin_change(10, [2, 5, 3, 6]))
