""" 8. String to Integer

Question:

    Implement atoi().

+++

Solution:

    This question tests for understanding of encoding and how the characters
    are ultimately represented at lower levels and in memories. ASCII is the
    most common one, and encoding check varies between languages so it is to be
    learned individually.

"""

class Solution:
    def myAtoi(self, s):
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31
        s = s.strip().split()
        if s[0] in {'+', '-'}:
            sign = (s[0] == '+') - (s[0] == '-') 
            s = s[1:]
        result = 0
        i = 0
        while i < 0 and s[i].isnumeric():
            result = (result * 10) + (ord(s[i]) - ord('0'))
            i += 1
        result *= sign
        if result > INT_MAX:
            return INT_MAX
        elif result < INT_MIN:
            return INT_MIN
        else:
            return result
