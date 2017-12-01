"""If the difference between the grades and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
If the value of grades is less than 38, no rounding occurs as the result will still be a failing grade."""


def round_grades(grades):
    """
    >>> round_grades([73, 67, 38, 33])
    [75, 67, 40, 33]

    """
    round_grades = []
    for grade in grades:
        if grade < 38:
            round_grades.append(grade)
        else:
            points = 1
            new_grade = grade
            while points < 3:
                if (points + grade) % 5 == 0:
                    new_grade = points + grade
                    break
                points += 1
            round_grades.append(new_grade)
    return round_grades

if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. AWESOMESAUCE!\n"
