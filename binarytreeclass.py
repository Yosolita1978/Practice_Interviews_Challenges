class BinaryTree(object):

    def __init__(self, root):

        self.root = root
        self.leftchild = None
        self.rightchild = None

    def insertLeft(self, new_node):

        if self.leftchild == None:
            self.leftchild == BinaryTree(new_node)
        else:

            t = BinaryTree(new_node)
            t.leftchild = self.leftchild
            self.leftchild = t

    def insertright(self, new_node):

        if self.rightchild == None:
            self.rightchild = BinaryTree(new_node)

        else:
            t = BinaryTree(new_node)
            t.rightchild = self.rightchild
            self.rightchild = t

    def getrightchild(self):
        return self.rightchild

    def getleftchild(self):
        return self.leftchild

    def setrootval(self, new_value):

        self.root = new_value

    def getrootval(self):

        return self.root


r = BinaryTree("a")
print r.getrootval()
print r.getleftchild()
print r.insertLeft("b").getrootval()