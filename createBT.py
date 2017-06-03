from binarytreeimplementation import BinaryTree


def balenced_tree(sorted_list):
    """Makes a tree from a sorted list recursively"""

    bt = BinaryTree()
    addNodes(bt, sorted_list, 0, len(sorted_list)-1)

    return bt


def addNodes(bt, sorted_list, low, high):
    """Adds nodes in a way that the BT is always balanced"""

    if low <= high:
        mid = (low+high)/2

        bt.add(sorted_list[mid])
        addNodes(bt, sorted_list, low, mid-1)
        addNodes(bt, sorted_list, mid+1, high)


x = range(10)
bt = balenced_tree(x)
print bt.root.value
print bt.root.left.value
print bt.root.right.value