""" 9. Palindrome Number

Question:

    Determine whether the given number is a palindrome.

+++

Solution:

    Simplest approach would be to reverse the integer and compare against the
    orignal. We may also check for cases that can screen out more than half of
    the inputs by checking for negative numbers, and those divisible by 10.

"""

class Solution:
    def reverse(self, num):
        result = 0
        while num:
            result = (result * 10) + (num % 10)
            num //= 10
        return result

    def isPalindromeNumber(self, num):
        if num != 0 and not num % 10 or num < 0:
            return False
        return self.reverse(num) == num
