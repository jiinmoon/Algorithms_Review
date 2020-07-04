""" 16. 3Sum Closest

Question:

    Given an array nums of n integers and an intger target, find three integers
    in nums such that the sum is closest to target. Return the sum of the three
    integers. You may assume that each input would hav exactly one solution.

+++

Solution:

    Similar approach from previous 3Sum problem can be utilized here. As we
    inspect the three elements chosen, we will compute their sum and compare
    against our closest variable.

"""

class Solution:
    def threeSumClosest(self, nums, target):
        m = len(nums)
        if not nums or m < 3:
            return None
        closest = float('-inf')
        nums.sort()
        for i in range(m-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = m-1
            while j < k:
                curr = (nums[i], nums[j], nums[k])
                currDiff = abs(target - sum(curr))
                prevDiff = abs(target - closest)
                closest = closest if prevDiff < currDiff else sum(curr)
                if sum(curr) < target:
                    j += 1
                else:
                    k -= 1
        return closest
