""" Implement a MyQueue class wich implements a queue usint two stacks. 
Problem 3.4 from Cracking the Coding Interview """


class Stack(object):
    """ This implements the Stack Class that we need to use"""
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return "%s" % (self.items,)


class MyQueue(object):

    def __init__(self):

        self.newest = Stack()
        self.oldest = Stack()

    def size(self):
        return self.newest.size() + self.oldest.size()

    def add(self, item):

        self.newest.push(item)

    def shift_stacks(self):

        while self.newest.size() > 0:
            self.oldest.push(self.newest.pop())

    def peek(self):

        self.shift_stacks()
        return self.oldest.peek()

    def remove(self):

        if self.oldest.size() == 0:
            self.shift_stacks()
        return self.oldest.pop()


if __name__ == "__main__":
    a = MyQueue()
    a.add(1)
    a.add(2)
    a.add(3)

    print a.size()
    print a.peek()
    print a.remove()
    print a.peek()
    print a.size()

