# 8 String to Integer

class Solution:
    def atoi(self, s):
        s = s.strip()
        if not s:
            return 0
        if s[0] == '+':
            sign = 1
            s.lstrip('+')
        elif s[0] == '-':
            sign = -1
            s.lstrip('-')

        result = 0
        i = 0
        while i < len(s) and s[i].isdigit():
            result *= 10 + (ord(s[i]) - ord('a'))
            i += 1
        
        result = sign * result
        if result >= 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif result < -2 ** 31:
            return -2 ** 31
        return result

