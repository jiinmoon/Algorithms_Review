""" 191. Number of 1 Bits """

class Solution:
    def hammingWeight(self, n):
        result = 0
        while n:
            result += n & 1
            n >>= 1
        return result
