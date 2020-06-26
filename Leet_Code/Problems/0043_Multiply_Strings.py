""" 43. Multiply Strings

Question:

    Given two non-negative integers num1 and num2 represented as strings, return
    the product of num1 and num2, also represented as a string.

"""

class Solution:
    def parseInt(self, num):
        result = 0
        for digit in num:
            result = result * 10 + ord(digit) - ord('0')
        return result

    def multiply(self, num1, num2):
        result = self.parseInt(num1) * self.parseInt(num2)
        return result
