""" Implement an algorith to determine if a string has all unique characters"""


def is_unique(string):
    """ Return Trus is a string has all unique characters or False if not

    >>> is_unique("")
    True

    >>> is_unique("Cat")
    True

    >>> is_unique("Cata")
    False

    >>> is_unique("23ds2")
    False
    """

    if len(string) > 128:
        return False

    unique = True
    char_dic = {}
    for char in string:
        if char not in char_dic:
            char_dic[char] = 1
    
        elif char in char_dic:
            unique = False
            return unique

    return unique

if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. AWESOMESAUCE!\n"
