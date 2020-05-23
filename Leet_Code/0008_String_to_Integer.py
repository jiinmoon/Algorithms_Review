""" 8. String to Integer

Question:

    Implement atoi which converts a string to an integer.

"""

class Solution:
    def parseInt(self, s):
        if not s:
            return 0

        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31
        result = 0
        sign = 1

        s = s.strip()

        if s[0] == '+':
            s = s[1:]
        elif s[0] == '-':
            sign = -1
            s = s[1:]

        while s and s[0].isnumeric():
            result = (result * 10) + (ord(s[0]) - ord('0'))
            s = s[1:]

        if result > INT_MAX:
            return INT_MAX
        elif result < INT_MIN:
            return INT_MIN
        else:
            return result
