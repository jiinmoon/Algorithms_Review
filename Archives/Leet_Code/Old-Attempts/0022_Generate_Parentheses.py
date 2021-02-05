""" 22. Generate Parentheses

Question:

    Given n pairs of parentheses, write a funnction to generate all combinations
    of well-formed parentheses.

"""

class Solution:
    def generateParenthesis(self, n):
        if n <= 0:
            return []

        result = []

        def backtrack(pairCount, openCount, path):
            if pairCount == openCount == 0:
                result.append(path)
                return
            if openCount > 0:
                backtrack(pairCount, openCount-1, path + ')')
            if pairCount > 0:
                backtrack(pairCount-1, openCount+1, path + '(')

        backtrack(n, 0, '')
        return result
