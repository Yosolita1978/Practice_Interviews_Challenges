""" You receive a list of tupples with the names of your employees. You have to do two things:
1. Find how is the CEO in the list of tupples
2. Form a tree with all your employees. Your CEO is the root of your tree

organization = [("Prakash", "Karen"), ("Prakash", "Sandheep"), ("Ryan", "Jair"), ("Shiva", "Prakash"), ("Shiva", "Ryan")]
Shiva
 Prakash
  Karen
  Sandheep
 Ryan
  Jair

"""

class Node(object):

    def __init__(self, name):
        self.name = name
        self.children = []


def print_tree(node, offset=0):

    print " " * offset + node.name
    for child in node.children:
        print_tree(child, offset+1)


def find_ceo(organization):
    """
    >>> organization = [("Prakash", "Karen"), ("Prakash", "Sandheep"), ("Ryan", "Jair"), ("Shiva", "Prakash"), ("Shiva", "Ryan")]
    >>> find_ceo(organization)
    'Shiva'
    """
    managment = set()
    employees = set()
    for pair in organization:
        managment.add(pair[0])
        employees.add(pair[1])

    ceo = list(managment - employees)[0]
    return ceo


def make_a_tree_organization(organization):

    """
    >>> organization = [("Prakash", "Karen"), ("Prakash", "Sandheep"), ("Ryan", "Jair"), ("Shiva", "Prakash"), ("Shiva", "Ryan")]
    >>> make_a_tree_organization(organization)
    Shiva
     Prakash
      Karen
      Sandheep
     Ryan
      Jair
    """

    # your need a dictionary to store all the names - nodes pairs
    nodes_dic = {}

    # here you're adding the child Nodes to the children list.
    for pair in organization:
        if pair[0] in nodes_dic:
            boss = nodes_dic[pair[0]]
        else:
            boss = Node(pair[0])
            nodes_dic[boss.name] = boss

        if pair[1] in nodes_dic:
            employee = nodes_dic[pair[1]]
        else:
            employee = Node(pair[1])
            nodes_dic[employee.name] = employee

        boss.children.append(employee)

    ceo = find_ceo(organization)
    root = nodes_dic[ceo]
    print_tree(root)


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. AWESOMESAUCE!\n"


