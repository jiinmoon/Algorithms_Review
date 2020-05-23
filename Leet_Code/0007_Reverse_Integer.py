""" 7. Reverse Integer

Question:

    Given 32-bit signed integer, reverse digits of an integer.

"""

class Solution:
    def reverseInt(self, num):
        sign = (num > 0) - (num < 0)
        num = abs(num)
        result = 0
        while num:
            result = (result * 10) + num % 10
            if result >= 2 ** 31 - 1:
                return 0
            num //= 10
        return sign * result
