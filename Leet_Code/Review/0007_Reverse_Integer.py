""" 7. Reverse Integer

Question:

    Reverse a given 32-bit interger, and watch out for overflows - return 0 if
    it does.

+++

Solution:

    A linear time solution is to simply repeatedly take the modulo to take last
    digit. The extra care is needed to handle the sign in the beginning.

"""

class Solution:
    def reverseInt(self, num):
        sign = (num > 0) - (num < 0)
        num = abs(num)
        result = 0
        while num:
            result = (result * 10) + (num % 10)
            if result > 2**31 - 1:
                return 0
            num //= 10
        return sign * result

