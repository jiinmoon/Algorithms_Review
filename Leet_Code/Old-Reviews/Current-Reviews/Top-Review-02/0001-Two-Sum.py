# 1 Two Sum

class Solution:
    def findTwoSum(self, nums, target):
        d = dict()
        for i, num in enumerate(nums):
            if num in d:
                return [ d[num], i ]
            d[target - num] = i
        return []
