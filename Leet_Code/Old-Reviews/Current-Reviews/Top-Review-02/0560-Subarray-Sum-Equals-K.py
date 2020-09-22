# 560 Subarray Sum Equals K

class Solution:
    def subarraysumEqualsK(self, nums, K):
        prefixSums = collections.defaultdict(int)
        runningSum = 0
        total = 0
        for num in nums:
            runningSum += num
            total += runningSum == K
            total += prefixSums[runningSum-K]
            prefixSums[runningSum] += 1
        return total
