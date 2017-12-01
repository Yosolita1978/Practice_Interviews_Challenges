"Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'. For this problem, you can falsely \"compress\" strings of single or double letters. For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes more space. \n"

def compress(string):
    """

    >>> compress("AAB")
    'A2B1'

    >>> compress("AAaa")
    'A2a2'

    >>> compress("AAAABBBBCCCCCDDEEEE")
    'A4B4C5D2E4'
    
    """
    r = ""
    l = len(string)

    if l == 0:
        return ""

    if l == 1:
        return string + "1"

    count = 1
    i = 1

    while i < l:

        if string[i] == string[i - 1]:
            count += 1
        else:
            r = r + string[i - 1] + str(count)
            count = 1

        i += 1

    r = r + string[i - 1] + str(count)

    return r

if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. AWESOMESAUCE!\n"





"""Cities to add:
Bangalore (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)"""

locations = {'North America': {'USA': ['Mountain View', "Atlanta"]},
             "Asia": {'China': ['Shanghai'],
                      'India': ['Bangalore']},
             'Africa': {'Egypt': ['Cairo']}
             }