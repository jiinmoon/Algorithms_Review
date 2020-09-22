# 15 3Sum
#
# Every k Sum problem is an extension of the 3Sum problem - for every element
# we choose, we can perform two pointer method to consider element combinations
# in O(n^2) instead of O(n^3). The problem is screening out the duplicate
# elements which are dealt with by sorting the given nums first.

class Solution:
    def find3Sum(self, nums):
        if len(nums) < 3:
            return []

        nums.sort()
        res = list()
        for i in range(len(nums)-2):
            if i != 0 and nums[i-1] == nums[i]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                curr = [nums[i], nums[j], nums[k]]
                if not sum(curr):
                    res.append(curr)
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]: j += 1
                    while j < k and nums[k] == nums[k+1]: k -= 1
                elif sum(curr) < 0:
                    j += 1
                else:
                    k -= 1

        return res
