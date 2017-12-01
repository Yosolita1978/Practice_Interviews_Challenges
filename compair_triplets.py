""" Write a function that takes two list of three elements and return the poins gained for each person.
    Comparison points is the total points a person earned.
    Given A and B, can you compare the two challenges and print their respective comparison points?"""


def compare_pairs(lst1, lst2):
    """ Returns the aumount of poits of each person

    >>> compare_pairs([5,6,7], [3,6,10])
    1 1

    >>> compare_pairs([3,2,1], [4,2,5])
    0 2

    >>> compare_pairs([4,2,5], [3,2,1])
    2 0
    """
    points_a, points_b = 0, 0
    compare = zip(lst1, lst2)
    for a, b in compare:
        if a > b:
            points_a += 1
        elif a < b:
            points_b += 1

    values = points_a, points_b

    for point in values:
        print point,


if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. AWESOMESAUCE!\n"
