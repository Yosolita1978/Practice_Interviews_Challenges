"""Return the longest palindrome in a string"""


def is_palindrome(s):
    """
    >>> is_palindrome("ozo")
    True

    >>> is_palindrome("a")
    True

    >>> is_palindrome("car")
    False
    """

    reverse = reversed(s)
    return s == "".join(reverse)


def longest_palindrome(s):
    #s is the string that contains the palindrome.
    """
    >>> longest_palindrome("ozono")
    'ozo'

    >>> longest_palindrome("adacracecar")
    'racecar'

    >>> longest_palindrome("francisco")
    'f'

    >>> longest_palindrome("ana")
    'ana'

    >>> longest_palindrome("a")
    'a'

    """

    queue = [s]

    while queue:
        seen = queue.pop(0)
        if is_palindrome(seen):
            return seen

        left = seen[:-1]
        right = seen[1:]
        queue.append(left)
        queue.append(right)


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. AWESOMESAUCE!\n"


