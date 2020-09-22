# 844 Backspace String Compare

class Solution:
    def backspaceCompare(self, S, T):
        def helper(s):
            stk = list()
            for char in s:
                if char != "#":
                    stk.append(char)
                elif stk:
                    stk.pop()
            return "".join(stk)

        return helper(S) == helper(T)
