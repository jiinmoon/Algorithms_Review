""" 136. Single Number

Question:

    Given a non-empty array of integers, every element appears twice except for
    one. Find that single one.

"""

class Solution:
    def findSingleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num # XOR cancels evenly occuring elements.
        return result
