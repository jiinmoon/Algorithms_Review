# 179 Largest Number
#
# We create a custom comparator that compares by string concatenation.

from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums):
        def larger(a, b):
            return -1 if a + b > b + a else 1

        nums = map(str, nums)
        nums.sort(key=cmp_to_key(larger))
        while nums and nums[0] == '0':
            nums = nums[1:]
        return "".join(nums)
