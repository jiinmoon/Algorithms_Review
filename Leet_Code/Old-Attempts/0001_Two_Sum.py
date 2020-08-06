""" 1. Two Sum

Question:

    Given an array of integers, return indicies of the two numbers such that
    they add up to a specific target.

    You may assume that each input would hav exactly one solution, and you may
    not use the same element twice.

+++

Solution:

    Naive approach would be to consider every element against others - going
    through all possible combinations that we can pick and choose the two
    elements to see whether it sums to target.

    Another approach would be to sort the given list of integers first - by
    doing so gives us a directionality on how to smartly choose our two elements
    - and able to find it in linear time. However, the sorting costs O(n lg n).

    Better approach is to utilize the extra space to record the (target - num)
    value. As we iterate, we have record of previously seen elements and we can
    find them in O(1). Thus, this would be a linear time complexity algorithm,
    achieved by trading space for time.

"""

class Solution:
    def twoSum(self, nums, target):
        if not nums:
            return []
        record = dict()
        for i, num in enumerate(nums):
            if num in record:
                return [record[num], i]
            else:
                record[target - num] = i
        return []
