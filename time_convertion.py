"""Given a time in -hour AM/PM format, convert it to military (-hour) time.

Examples::

    >>> convert_time("07:05:45PM")
    19:05:45

    >>> convert_time("07:05:45AM")
    07:05:45

    >>> convert_time("12:05:45AM")
    00:05:45

    >>> convert_time("12:05:45PM")
    12:05:45
"""


def convert_time(time):
    hour_str = time[0:2]
    num_hour = int(hour_str)
    rest = time[2:8]
    suffix = time[8:]

    if suffix == "AM" and num_hour < 12:
        print '%s%s' % (hour_str, rest)

    elif suffix == "AM" and num_hour == 12:
        hour_str = "00"
        print '%s%s' % (hour_str, rest)

    if suffix == "PM" and num_hour == 12:
        print '%s%s' % (hour_str, rest)

    elif suffix == "PM" and num_hour < 12:
        num_hour = num_hour + 12
        print '%i%s' % (num_hour, rest)




if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. AWESOMESAUCE!\n"