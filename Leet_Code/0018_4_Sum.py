""" 18. 4 Sum

Question:

    Given an array nums of n integers and an integer target, are there elements
    a, b, c, and d in nums such that that sum up to target? Find all unique
    quadruplets in the array which gives the sum of target.

+++

Solution:

    Again, this problem can be seen as a expansion of two sum problem. However,
    we will use boundary checks to reduce the time further.

"""

class Solution:
    def findFourSum(self, nums, target):
        if not nums or len(nums) < 4:
            return []

        result = set()
        nums.sort()
        m = len(nums)

        for i in range(m-3):
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target or \
                nums[i] + nums[m-1] + nums[m-2] + nums[m-3] < target:
                continue
            for j in range(i+1, m-2):
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target or \
                    nums[i] + nums[j] + nums[m-1] + nums[m-2] < target:
                    continue
                k, l = j + 1, m - 1
                while k < l:
                    curr = (nums[i], nums[j], nums[k], nums[l])
                    if sum(curr) == target:
                        result.add(curr)
                        k += 1
                        l -= 1
                        while k < l and nums[k] == nums[k-1]:
                            k += 1
                        while k < l and nums[l] == nums[l+1]:
                            l -= 1
                    elif sum(curr) < target:
                        k += 1
                    else:
                        l -= 1

        return list(result)
