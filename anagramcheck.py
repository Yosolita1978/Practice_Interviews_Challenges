"""Given two strings, check to see if they are anagrams. 
An anagram is when the two strings can be written using the exact same letters 
(so you can just rearrange the letters to get a different phrase or word).

Examples::

    >>> check_anagram('dog','god')
    True

    >>> check_anagram('clint eastwood','old west action')
    True

    >>> check_anagram('aa','bb')
    False

"""


def check_anagram(string1, string2):
    """Are the two words anagrams?"""

    s1 = string1.replace(" ", "").lower()
    s2 = string2.replace(" ", "").lower()

    #easy fall, because they have different number of letters
    if len(s1) != len(s2):
        return False

    count_letters = {}
    # with the first string we add the letters to the dictionary
    for letter in s1:
        if letter in count_letters:
            count_letters[letter] += 1
        else:
            count_letters[letter] = 1

    # with the second string we rest all the letters, so the dictionary should be zero for all the letters
    for letter in s2:
        if letter in count_letters:
            count_letters[letter] -= 1
        else:
            count_letters[letter] = 1

    #Here we check that all the values in dic are zero
    for key in count_letters:
        if count_letters[key] != 0:
            return False

    return True


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. AWESOMESAUCE!\n"


