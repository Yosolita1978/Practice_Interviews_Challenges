import ctypes


class DynamicArray(object):

    def __init__(self):

        #n are the elements in the array
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):

        return self.n

    def __getitem__(self, k):

        if not 0 <= k < self.n:
            return IndexError("K is out of bounds!")

        return self.A[k]

    def append(self, element):
        #Add a element to the end of the array. This is the key method. 

        if self.n == self.capacity:
            self._resize(2*self.capacity)

        self.A[self.n] = element
        self.n += 1

    def _resize(self, new_cap):

        B = self.make_array(new_cap)

        for k in range(self.n):
            B[k] = self.A[k]

        self.A = B
        self.capacity = new_cap

    def make_array(self, new_cap):

        return (new_cap * ctypes.py_object)()


"**************************************************"

""" This excersice is a reference to this problem in Hacker Rank
https://www.hackerrank.com/challenges/dynamic-array

N = Number of sequences
Q = Number of queries

Each Q contains a query in the format:

1. Query 1 x y
Find the sequence at index '((x ^ lastAns)%\N)'' in the sequences list
Append integer y to the sequence

2. Query 2 x y
Find the sequences at index ((x ^ lastAns) %\N) in the sequences list
Fin the value y %\size in sequence (size is the len of sequence) and assign to lastAns
print the value of lastAns in a new line


"""


first_line_input = [2, 5]

queries = {"1": [1, 0, 5],
           "2": [1, 1, 7],
           "3": [1, 0, 3],
           "4": [2, 1, 0],
           "5": [2, 1, 1]}

N = first_line_input[0]
Q = first_line_input[1]

lastAns = 0
list_of_sequences = [[]] * N

for trial in range(1, Q + 1):
    i = str(trial)
    query = queries[i][0]

    if query == 1:
        index = (queries[i][1] ^ lastAns) % N
        list_of_sequences[index] = list_of_sequences[index] + [queries[i][2]]

    else:
        index = (queries[i][1] ^ lastAns) % N
        number = queries[i][2] % len(list_of_sequences[index])
        lastAns = int(list_of_sequences[index][number])

        print lastAns





















