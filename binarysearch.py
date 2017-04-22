""" Implement an algorith to find and item in a list using binary search"""


def binary_search(lst, item):
    """ Return the index of the item in a list, using binary search or return -1 if that items is not in the list

    >>> binary_search([1,3,5,7,9], 3)
    1

    >>> binary_search([1,3,5,7,9], -1)
    -1

    
    """
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high)
        guess = lst[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return -1

if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. AWESOMESAUCE!\n"