""" Find the shortest path in a hash of options
You will need 3 helper functions: - total_cost, find_permutations and find_the_shortest_path"""


PATHS = {'A': {'D': 1, 'B': 3},
         'D': {'A': 1, 'E': 2,  'C': 8},
         'B': {'A': 3, 'C': 2,  'X': 4, 'Y': 3},
         'C': {'B': 2, 'X': 15, 'D': 8, 'E': 2},
         'X': {'B': 4, 'Y': 1, 'C': 15},
         'Y': {'X': 1, 'B': 3},
         'E': {'D': 2, 'C': 2},
         }


def final_cost(path):
    """ The path is an array in the form ['A', 'B', 'X']"""
    cost = 0
    for i in xrange(len(path) - 1):
        cost += PATHS[path[i]][path[i + 1]]
    return cost

# print final_cost(['A', 'B', 'X'])


def all_permutations(start, finish, seen=[]):
    """ Find with recursion all the posibles permutation from a start point to the finish point"""
    p = []
    if start == finish:
        return [[start]]

    for next in PATHS[start].keys():
        if next not in seen:
            for per in all_permutations(next, finish, seen + [start]):
                p.append([start] + per)

    return p

#print all_permutations('A', 'E')
# [['A', 'B', 'X', 'C', 'E'], ['A', 'B', 'X', 'C', 'D', 'E'], ['A', 'B', 'C', 'E'], ['A', 'B', 'C', 'D', 'E'], ['A', 'B', 'Y', 'X', 'C', 'E'], ['A', 'B', 'Y', 'X', 'C', 'D', 'E'], ['A', 'D', 'C', 'E'], ['A', 'D', 'E']]


def fin_shortest_path(start, finish):
    """ Grab all the posibles paths between two spots and find the shipper path"""

    small_cost = None
    per = all_permutations(start, finish)
    shortest = None
    for p in per:
        cost = final_cost(p)
        if cost < small_cost or small_cost is None:
            small_cost = cost
            shortest = p

    return shortest


# print fin_shortest_path('A', 'E')
# ['A', 'D', 'E']