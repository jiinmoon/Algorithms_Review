""" 15. 3Sum

Question:

    Given a list of integers, find all unique cominations of three elements
    that sums to 0.

+++

Solution:

    Instead of naive solution where we would compare and choose every element
    combinations, which would result in O(n^3) time complexity, we will first
    sort the given list. By doing so, it gives us a directionality to use two
    pointer method - which reduces the overall time complexity to O(n lg n).

    We have to be watchful for avoiding selecting duplicate sets - this can be
    done in either using a data structure that does not accpet duplicate such
    as set or avoid choose duplicates when we are conidering our candidates.

"""

class Solution:
    def threeSum(self, nums):
        m = len(nums)
        if not nums or m < 3:
            return []
        result = set()
        nums.sort()
        for i in range(m-2):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            j = i+1
            k = m - 1
            while j < k:
                curr = (nums[i], nums[j], nums[k])
                if not sum(curr):
                    result.add(curr)
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                elif sum(curr) < 0:
                    j += 1
                else:
                    k -= 1
        return list(result)

