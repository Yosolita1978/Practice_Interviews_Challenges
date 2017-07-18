""" From cracking the coding interviw pag 150 problem 10.3"""


def find(lst, target):
    return findHelper(lst, 0, len(lst)-1, target)


def findHelper(lst, left, right, target):
    mid = (left + right)//2
    if target == lst[mid]:
        return mid
    if right < left:
        return -1

    if lst[left] < lst[mid]:
        if (target >= lst[left] and target < lst[mid]):
            return findHelper(lst, left, mid-1, target)
        else:
            return findHelper(lst, mid+1, right, target)
    elif lst[mid] < lst[left]:
        if target > lst[mid] and target <= lst[right]:
            return findHelper(lst, mid+1, right, target)
        else:
            return findHelper(lst, left, mid-1, target)
    elif lst[left] == lst[mid]:
        if lst[mid] != lst[right]:
            return findHelper(lst, mid+1, right, target)
        else:
            result = findHelper(lst, left, mid-1, target)
            if result == -1:
                return findHelper(lst, mid+1, right, target)
            else:
                return result
    return -1

lst = [15, 16, 19, 20, 25, 1, 3, 4, 5, 5, 5,  5, 7, 10, 14]
lst2 = [15, 16, 19, 20, 25, 1, 3, 3, 3, 4, 5, 7]
lst3 = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 13, 14]
lst4 = [2, 2, 2, 3, 4, 2]
index = find(lst, 5)
index1 = find(lst2, 5)
index2 = find(lst3, 5)
index3 = find(lst4, 2)
print index, index1, index2, index3