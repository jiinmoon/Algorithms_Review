""" 22. Generate Parentheses

Question:

    Given integer n, return all possible well-formed parentheses.

+++

Solution:

    We will utilize the backtracking algorithm to explore all the possible ways
    that we can form valid parentheses. To do so, we will need to maintain
    current status: how many open parentheses are left to still be closed, and
    how many more parentheses still need to be added, and the path that we are
    building.

"""

class Solution:
    def generateParentheses(self, n):
        if not n:
            return []
        result = []
        
        def backtrack(pairCount, openCount, path):
            if not pairCount and not openCount:
                result.append(path)
                return
            if openCount:
                backtrack(pairCount, openCount-1, path + ')')
            if pairCount:
                backtrack(pairCount-1, openCount+1, path + '(')
        
        backtrack(n, 0, '')
        return result

