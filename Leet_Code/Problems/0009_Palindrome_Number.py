""" 9. Palindrome Number

Question:

    Determine whether an integer is a plaindrome. An integer is a palindrome
    when it reads the same backward as forward.

+++

Solution:

    We can begin by asking which numbers cannot be palindrome - negative
    integers and numbers that are evenly divisible by 10 cannot be palindrome.
    Then, simple way to check for palindrome would be to reverse the integer
    then compare against the original number.

"""

class Solution:
    def reverseInt(self, num):
        result = 0
        while num:
            result = (result * 10) + (num % 10)
            num //= 10
        return result

    def isPalindrome(self, num):
        if not num:
            return True
        if num < 0 or num % 10 == 0:
            return False
        return self.reverseInt(num) == num
