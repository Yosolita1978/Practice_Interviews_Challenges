"""Given the months of the calendar, and a number, find what day of that year it is"

Examples::

    >>> find_day(31)
    ('January', 31)

    >>> find_day(15)
    ('January', 15)

    >>> find_day(45)
    ('February', 14)

    >>> find_day(368)


    >>> find_day(145)
    ('May', 25)
"""


def find_day(number):

    calendar = [('January', 31), ('February', 28), ('March', 31), ('April', 30), ('May', 31), ('June', 30), ('July', 31), ('August', 31), ('September', 30), ('October', 31), ('November', 30), ('December', 31)]

    for month in calendar:
        name, days = month
        if number <= days:
            date = (name, number)
            return date

        else:
            number = number - days

    return None


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. AWESOMESAUCE!\n"

