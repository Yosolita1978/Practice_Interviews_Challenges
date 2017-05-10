def max_sum(array):
    "Find the  maximun sum on all the sublist in an array"

    n = len(array)
    mxm = 0

    for i in xrange(0, n):
        current_sum = 0
        for j in xrange(i, n):
            current_sum += array[j]
            if current_sum > mxm:
                mxm = current_sum

    return mxm


print max_sum([-2, 11, -4, 13, -5, 2])


def maxSubArray(ls):
    "another form of find the maximun sum"
    if len(ls) == 0:
        raise Exception("Array empty")  # should be non-empty

    runSum = maxSum = ls[0]
    i = 0
    start = finish = 0

    for j in range(1, len(ls)):
        if ls[j] > (runSum + ls[j]):
            runSum = ls[j]
            i = j
        else:
            runSum += ls[j]

        if runSum > maxSum:
            maxSum = runSum
            start = i
            finish = j

    print "maxSum =>", maxSum
    print "start =>", start, "; finish =>", finish

maxSubArray([-2, 11, -4, 13, -5, 2])


def print_valid_parenthesis(n, left=0, right=0, string=""):

    if left == right and right == n:
        return {string}

    results = set()

    if left > right:
        results.update(print_valid_parenthesis(n, left, right + 1, string + ")"))

    if left < n:
        results.update(print_valid_parenthesis(n, left + 1, right, string + "("))

    return results

print print_valid_parenthesis(5)










