"""Given two strings write a method to decide if one is a permutation of the other"""


def check_permutation(string1, string2):
    """ Returns True if the two strings are permutations

    >>> check_permutation("abc", "cba")
    True

    >>> check_permutation("abcq", "cbaa")
    False
    """

    if len(string1) != len(string2):
        return False

    return "".join(sorted(string1)) == "".join(sorted(string2))


def write_permutation(lst):
    """ Return all the posibles permutations of a string with recursion """ 

    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return [lst]
    else:
        l = []
        for i in range(len(lst)):
            x = lst[i]
            rest = lst[:i] + lst[i+1:]
            for option in write_permutation(rest):
                l.append([x] + option)
        return l

data = list("123")
for option in write_permutation(data):
    print option


if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. AWESOMESAUCE!\n"
