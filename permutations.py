from itertools import permutations

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


def number_perms(obj):
    "Find the number of permutations that a string have. I don't have to do the permutations, just find the number"
    perm_set = set()
    for item in permutations(str(obj)):
        if item not in perm_set:
            perm_set.add(item)
    return len(perm_set)

obj = "12345"
print number_perms(obj)



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

#If I want to use that fuction to know how many numbers of permutations could be done in a string
data = list("12345")
perm = []
for option in write_permutation(data):
    if option not in perm:
        perm.append(option)
number = len(perm)
print number


if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. AWESOMESAUCE!\n"
