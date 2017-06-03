""" Binary Tree and Binary Search Implementation"""


class BinaryNode(object):

    def __init__(self, value=None):
        """Create Binary Node """

        self.value = value
        self.left = None
        self.right = None

    def add(self, val):
        """Adds a new node to the tree containing this value"""

        if val <= self.value:
            if self.left:
                self.left.add(val)
            else:
                self.left = BinaryNode(val)
        else:
            if self.right:
                self.right.add(val)
            else:
                self.right = BinaryNode(val)

    def delete(self):
        """Remove value of the self from BT"""

        if self.left == self.right == None:
            return None
        if self.left == None:
            return self.right

        if self.right == None:
            return self.left

        child = self.left
        grandchild = child.right
        if grandchild:
            while grandchild.right:
                child = grandchild
                grandchild = child.right
            self.value = grandchild.value
            child.right = grandchild.left
        else:
            self.left = child.left
            self.value = child.value

        return self


class BinaryTree(object):

    def __init__(self):
        """Create empty binary Tree"""
        self.root = None

    def add(self, val):
        """Insert value intro proper location in BT"""
        if self.root is None:
            self.root = BinaryNode(val)
        else:
            self.root.add(val)

    def contains(self, target):
        """Check whether BST contains a target value"""

        node = self.root
        while node:
            if target == node.value:
                return True

            if target < node.value:
                node = node.left

            else:
                node = node.right

        return False

    def remove(self, value):
        """Remove value from Tree"""

        if self.root:
            self.root = self.removeFromParent(self.root, value)

    def removeFromParent(self, parent, value):
        """Remove value from tree rooted at parent"""

        if parent is None:
            return None

        if value == parent.value:
            return parent.delete()
        elif value < parent.value:
            parent.left = self.removeFromParent(parent.left, value)
        else:
            parent.right = self.removeFromParent(parent.right, value)

        return parent