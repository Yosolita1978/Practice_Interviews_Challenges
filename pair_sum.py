"""Given an integer array, output all the unique pairs that sum up to a specific value k.

Examples::

    >>> pair_sum([1,3,2,2],4)
    [(1, 3), (2, 2)]
    2

    >>> pair_sum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10)
    [(5, 5), (2, 8), (-1, 11), (1, 9), (3, 7), (4, 6)]
    6

    >>> pair_sum([1,2,3,1],3)
    [(1, 2)]
    1
"""

def pair_sum(lst, k):

    if len(lst) < 2:
        return "You list is to small"

    seen = set()
    output = set()

    for num in lst:
        target = k - num
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(target, num), max(target, num)))

    print list(output)
    return len(output)


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. AWESOMESAUCE!\n"

