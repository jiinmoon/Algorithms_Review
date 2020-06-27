""" Single Number

Solution:

    To find the single element among duplicates, we may count each elements -
    which will require O(n) time and space. However, we can save space by simply
    leveraging bit operation XOR - which cancels out the duplicate elements.

"""

class Solution:
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num
        return result
