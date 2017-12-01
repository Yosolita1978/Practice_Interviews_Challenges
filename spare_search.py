""" From Cracking the Coding Interview pag 150. Problem 10.5"""


def binSearch(lst, left, right, target):
    mid = (left + right)/2
    if target == lst[mid]:
        return mid
    if right < left:
        return -1
    if lst[mid] == "":
        ret1 = binSearch(lst, left, mid-1, target)
        if ret1 != -1:
            return ret1
        else:
            return binSearch(lst, mid+1, right, target)
    else:
        if target > lst[mid]:
            return binSearch(lst, mid+1, right, target)
        else:
            return binSearch(lst, left, mid-1, target)

lst = ["at", "", "", "", "ball", "",  "", "car", "", "", "dad", "", ""]
print binSearch(lst, 0, len(lst)-1, "ball")
