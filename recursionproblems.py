def sum_recursive(lst):
    if len(lst) == 0:
        return 0
    suma = lst[0] + sum_recursive(lst[1:])
    return suma

print sum_recursive([2, 4, 6])


def count_recursive(lst):
    if lst == []:
        return 0
    return 1 + count_recursive(lst[1:])

print count_recursive([2, 4, 6])


def max_num_recursive(lst):
    if len(lst) == 2:
        return lst[0] if lst[0] > lst[1] else lst[1]
    sub_max = max_num_recursive(lst[1:])
    return lst[0] if lst[0] > sub_max else sub_max

print max_num_recursive([2, 24, 6])

def quicksort_recursive(array):

    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]

        greater = [i for i in array[1:] if i > pivot]

        return quicksort_recursive(less) + [pivot] + quicksort_recursive(greater)

print quicksort_recursive([10, 5, 2, 3, 24])