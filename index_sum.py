"""Given an array of integers, return indices of the two numbers such that they add up to a specific target.

Examples::

    >>> pair_index_sum([3,2,4],6)
    [1, 2]

    >>> pair_index_sum([2, 7, 11, 15],9)
    [0, 1]

    >>> pair_index_sum([-3,4,3,90],0)
    [2, 0]
"""


def pair_index_sum(nums, target):

    index_dic = {}
    for i in range(len(nums)):
        if nums[i] not in index_dic:
            index_dic[nums[i]] = i

    output_index = []
    for key, value in index_dic.items():
        complement = target - key
        
        if complement in index_dic:
            output_index.append(index_dic[key])
            output_index.append(index_dic[complement])

            return output_index

if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. AWESOMESAUCE!\n"
