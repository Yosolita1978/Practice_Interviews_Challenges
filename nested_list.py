"""Given the names and grades for each student in a Physics class of  students, 
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Examples::

    >>> find_second([['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]])
    Berry
    Harry
"""

def find_second(lst):
    students = {}
    for student in lst:
        name, score = student
        if score in students:
            students[score].append(name)
        else:
            students[score] = [name]
    
    scores = list(students.keys())
    scores.sort()
    for i in sorted(students[scores[1]]):
        print i


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. AWESOMESAUCE!\n"
