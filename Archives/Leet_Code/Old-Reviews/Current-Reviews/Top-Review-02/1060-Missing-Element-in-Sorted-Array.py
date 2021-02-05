# 1060 Missing Element in Sorted Array

class Solution:
    def missingElement(self, nums, k):
        nums.append(float('inf'))
        for i in range(1, len(nums)+1):
            prev, curr = nums[i-1], nums[i]
            offset = curr - prev - 1
            if k - offset <= 0:
                return prev + k
            k -= offset
        return -1
