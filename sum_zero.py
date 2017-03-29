""" Write a function that takes a list and return a list of tupples with all the pairs that sum zero"""


def count_zero_pairs(lst):
    """ Returns a list of tupples with all the pairs that sum zero

    >>> count_zero_pairs([1, 2, 3, -3, -2])
    [(2, -2), (3, -3)]

    >>> count_zero_pairs([])
    []

    >>> count_zero_pairs([1, 2, -3, 3, -2, -1])
    [(1, -1), (2, -2), (3, -3)]

    """

    list_tupples = []

    if len(lst) == 0:
        return list_tupples

    tupple_num = ()
    for num in lst:
        if num > 0:
            if - num in lst:
                tupple_num = (num, -num)
                list_tupples.append(tupple_num)

    return list_tupples


if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. AWESOMESAUCE!\n"