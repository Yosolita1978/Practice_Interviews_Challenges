"""You're going to write a function that returns True if two words are isomorphic or False, otherwise.

Your function should take two strings and return False or True. 
For example is_isomorphic("foo", "bar") return False because the o is coding to a in the first case, and then to r. 
is_isomorphic("mom", "dad") returns True because the coding of letters match """


def is_isomorphic(str1, str2):
    """

    >>> is_isomorphic("mom", "dad")
    True

    >>> is_isomorphic("foo", "bar")
    False

    >>> is_isomorphic("cat", "zip")
    True
    
    """
    letter_dic = {}
    for index, letter in enumerate(str1):
        if letter not in letter_dic:
            letter_dic[letter] = str2[index]

        if letter_dic[letter] != str2[index]:
            return False

    return True

if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. AWESOMESAUCE!\n"