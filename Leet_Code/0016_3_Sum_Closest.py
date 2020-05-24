""" 16. 3 Sum Closest

Question:

    Given an array nums of n integers and an integer target, find three integers
    in nums such that the sum is closest to target. Return the sum of the three
    integers, You may assume that each input would have exactly one solution.

"""

class Solution:
    def findThreeSumClosest(self, nums, target):
        if not nums or len(nums) < 3:
            return 0
        closest = float('-inf')
        nums.sort()
        result = []
        for i, A in enumerate(nums[:-2]):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                curr = [ A, nums[j], nums[k] ]
                diff = abs(target - sum(curr))
                if diff < closest:
                    result = curr
                    closest = diff
                if sum(curr) < target:
                    j += 1
                else:
                    k -= 1
        return sum(result)

