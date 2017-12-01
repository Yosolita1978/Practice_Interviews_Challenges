""" Make the whole implementation of a Tree using just lists """


def BinaryTree(root):
    return [root, [], []]


def insertLeft(root, new_branch):

    t = root.pop(1)

    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])

    return root


def insertRight(root, new_branch):

    t = root.pop(2)

    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])

    return root


def findroot(root):
    return root[0]


def setnewroot(root, new_val):
    root[0] = new_val


def getleftchild(root):
    return root[1]


def getrightchild(root):
    return root[2]


r = BinaryTree(3)
insertLeft(r, 4)
insertLeft(r, 5)
insertRight(r, 6)
insertRight(r, 7)

print r