# 946 Validate Stack Sequences

class Solution:
    def isValid(self, pushed, popped):
        popped.reverse()
        stk = list()
        for x in pushed:
            stk.append(x)
            while stk and popped and stk[-1] == popped[-1]:
                stk.pop()
                popped.pop()
        return not popped
