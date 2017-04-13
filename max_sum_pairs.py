"""Given an integer array, output all the unique pairs that sum up to the max_sum in the array.

Examples::

    >>> pair_max_sum([1,3,2,2])
    (3, 2)
    >>> pair_max_sum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1])
    (13, 14)
    >>> pair_max_sum([1,2,5,1])
    (2, 5)
"""


def pair_max_sum(lst):

    if len(lst) < 2:
        return "You list is to small"

    max_sum = 0
    tupple_dic = {}
    for i in range(len(lst) - 1):
        tupple = (lst[i], lst[i + 1])
        sum_tupple = sum(tupple)
        tupple_dic[sum_tupple] = tupple

    for key, value in tupple_dic.items():
        if key > max_sum:
            max_sum = key
    
    return tupple_dic[max_sum]

if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. AWESOMESAUCE!\n"

