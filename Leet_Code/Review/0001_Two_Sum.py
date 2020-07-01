""" 1. Two Sum

Question:

    Given an array of integers, return indices of the two numbers such that
    they add up to a specific target.

+++

Solution:

    Naive approach would be to use a nested-loop in order to compare each
    element against one another - trying out all possible combinations. Even
    with the improvement of not looking back strategy, this is an O(n^2)
    algorithm

    Sorting makes the array to have a directionality; that is, we may use two
    pointer method in order to find the two elements in logical way from the
    either end of the array. The searching along should only take O(n),
    however, the sorting is bounded by O(n lg n), which determines the overall
    complexity.

    Then, we look to trade space for time. Once we seen a variable, we do not
    have to go back to search for it, if we can store it in a storage where
    fast look-up is allowed such as hashmap structure (dictionary or set in
    Python).

"""

class Solution:
    def findTwoSum(self, nums, target):
        if not nums or len(nums) < 2 or target < sum(nums) < target:
            return []
        record = dict()
        for i, num in enumerate(nums):
            if num in record:
                return [record[num], i]
            record[target - num] = i
        return []

