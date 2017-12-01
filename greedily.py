"""Write an efficient function that takes stock_prices_yesterday and returns the best profit I could have made 
from 1 purchase and 1 sale of 1 Apple stock yesterday.

For example:
stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
returns 6 (buying for $5 and selling for $11)

"""

"First solution using a little of force brute"


def get_max_profit(stock_prices_yesterday):
    """
    >>> stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
    >>> get_max_profit(stock_prices_yesterday)
    6

    """

    #my function receive as parameter the whole list of prices
    min_price = stock_prices_yesterday[0]
    max_profit = 0

    for current_price in stock_prices_yesterday:

        # ensure min_price is the lowest price we've seen so far
        min_price = min(min_price, current_price)

        # see what our profit would be if we bought at the
        # min price and sold at the current price
        potential_profit = current_price - min_price

        # update max_profit if we can do better
        max_profit = max(max_profit, potential_profit)

    return max_profit

"Second solution using the greedly algorithm"

def get_max_profit(stock_prices_yesterday):

    """
    >>> stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
    >>> get_max_profit(stock_prices_yesterday)
    6

    >>> stock_prices_yesterday = []
    >>> get_max_profit(stock_prices_yesterday)
    IndexError('Getting a profit requires at least 2 prices')

    >>> stock_prices_yesterday = [10, 7, 5, 8, -11, 9]
    >>> get_max_profit(stock_prices_yesterday)
    20

    """

    # make sure we have at least 2 prices
    if len(stock_prices_yesterday) < 2:
        raise IndexError('Getting a profit requires at least 2 prices')

    # we'll greedily update min_price and max_profit, so we initialize
    # them to the first price and the first possible profit
    min_price = stock_prices_yesterday[0]
    max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]

    for index, current_price in enumerate(stock_prices_yesterday):

        # skip the first (0th) time
        # we can't sell at the first time, since we must buy first,
        # and we can't buy and sell at the same time!
        # if we took this out, we'd try to buy *and* sell at time 0.
        # this would give a profit of 0, which is a problem if our
        # max_profit is supposed to be *negative*--we'd return 0!
        if index == 0:
            continue

        # see what our profit would be if we bought at the
        # min price and sold at the current price
        potential_profit = current_price - min_price

        # update max_profit if we can do better
        max_profit = max(max_profit, potential_profit)

        # update min_price so it's always
        # the lowest price we've seen so far
        min_price = min(min_price, current_price)

    return max_profit

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. AWESOMESAUCE!\n"

