def greedy_coin_change(amount, coins):
    """
    Return a list of coins that add up to the amount using a greedy strategy.
    Assumes coins are sorted in descending order.
    """
    result = []
    for coin in coins:
        while amount >= coin:
            amount -= coin
            result.append(coin)
    return result

# coin denominations (sorted descending)
coins = [25, 10, 5, 1]
amount = 68 # For example, 68 cents
change = greedy_coin_change(amount, coins)
print("Coins used for 68 cents (greedy):", change)