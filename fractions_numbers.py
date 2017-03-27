"""Given an array of integers, calculate which fraction of its elements are positive,
    which fraction of its elements are negative, and which fraction of its elements are zeroes,
    respectively. Print the decimal value of each fraction on a new line."""


def count_numbers(array, n):
    """ Print the fraction of the positives, negatives and zeros in an array

    >>> arr = [-4, 3, -9, 0, 4, 1]
    >>> n = 6
    >>> count_numbers(arr, n)
    0.500000
    0.333333
    0.166667

    """
    fractions = []
    positives = 0.0
    negatives = 0.0
    zeros = 0.0
    for num in array:
        if num < 0:
            negatives += 1
        elif num == 0:
            zeros += 1
        elif num > 0:
            positives += 1
    
    positive_fraction = positives / n
    fractions.append(positive_fraction)
    negative_fraction = negatives / n
    fractions.append(negative_fraction)
    zeros_fraction = zeros / n
    fractions.append(zeros_fraction)
    
    for num in fractions:
        print '%6f' % (num)

if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. AWESOMESAUCE!\n"
