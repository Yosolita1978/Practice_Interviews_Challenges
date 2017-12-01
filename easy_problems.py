def sum_nums1(n):
    """ Returns the sum of all the numbers in a list with n items 

    >>> sum_nums1(10)
    55

    >>> sum_nums1(5)
    15
    """
    final_sum = 0 

    for x in xrange(n+1):
        final_sum += x

    return final_sum

def sum_nums2(n):
    """It does the same thing but faster with an algorithm"""
    return (n*(n+1))/2

if __name__ == "__main__":
    import doctest
    doctest.testmod()
