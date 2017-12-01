"Print the absolute difference between the two sums of the matrix's diagonals as a single integer"


def sum_right(matrix, n):
    """ Find the value for the right diagonal in the matrix

    >>> matrix = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
    >>> sum_right(matrix, 3)
    4
    """
    total = 0
    for i in range(n):
        total += matrix[i][i]
    return total


def sum_left(matrix, n):
    """ Find the value for the left diagonal in the matrix

    >>> matrix = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
    >>> sum_left(matrix, 3)
    19

    """
    total = 0
    for i in range(n):
        j = n - 1 - i
        total += matrix[i][j]
    return total


def rest_values(x, y):
    """ Return the absolute difference between two values

    >>> matrix = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
    >>> right = sum_right(matrix, 3)
    >>> left = sum_left(matrix, 3)
    >>> rest_values(right, left)
    15
    """
    return abs(x-y)

if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. AWESOMESAUCE!\n"
