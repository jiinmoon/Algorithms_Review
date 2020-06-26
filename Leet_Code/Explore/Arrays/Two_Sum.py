""" Two Sum

Solution:

    Naive approach would be to compare every element against each other. Even
    with the improvement of ignoring previous compared elements, this results in
    O(n^2) time complexity.

    Slightly improved approach would be to first, sort the given array. Then, we
    may use two pointer method where the pointers start from each end as sorted
    array now has an dirctionality - we know whether we should move lo or hi
    pointer depending on current sum. While two pointer method is linear,
    because of sorting, it still costs overall O(n lg n).

    The linear time-complexity can be achieved by trading space - we use hashmap
    structure to record the values that we have seen thus far.

"""

class Solution:
    def findTwoSum(self, nums, target):
        m = len(nums)
        if not m or m < 2:
            return None

        record = dict()
        for i, num in enumerate(nums):
            if num in record:
                return [nums[num], i]
            reocrd[target - num] = i
        return []

