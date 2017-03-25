""" Write a function that takes a word an return True or False
    if tht word has more vowels than non_vowels or viceversa """


def count_vowels(word):
    """ Returns True or False if the number of vowels is bigger

    >>> count_vowels("Cat")
    False

    >>> count_vowels("Moon")
    True

    >>> count_vowels("You")
    True
    """
    vowels = {"a", "e", "i", "o", "u"}
    count_v = 0
    len_word = len(word)

    for letter in word:
        if letter in vowels:
            count_v += 1

    if len_word % 2 == 0:
        midle = len_word / 2
        if count_v >= midle:
            return True
    else:
        midle = len_word / 2 + 1
        if count_v >= midle:
            return True

    return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()