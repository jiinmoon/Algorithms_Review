""" 190. Reverse Bits """

class Solution:
    def reverseBits(self, n):
        """ n is 32-bits unsigned integer. """
        result = 0
        for i in range(31):
            rightMostBit = n & 1
            result = result | rightMostBit
            result <<= 1
            n >>= 1
        return result | n # don't forget the last bit.
