# alpha = ["a", "b", "c", "d"]

# for first in alpha:
#     for second in alpha:
#         if second == first:
#             continue
#         for third in alpha:
#             if third == first or third == second:
#                 continue
#             for fourth in alpha:
#                 if fourth == first or fourth == second or fourth == third:
#                     continue
#                 print first + second + third + fourth


def permutations(alpha, n):

    prefixes = [[]]

    for i in range(n):
        new_prefixes = []
        for prefix in prefixes:

            for element in alpha:
                if element in prefix:
                    continue
                new_prefixes.append(prefix + [element])

        prefixes = new_prefixes

    return prefixes


print permutations(["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"], 10)
