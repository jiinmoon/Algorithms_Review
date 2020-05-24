""" 20. Valid Parentheses

Question:

    Given a string containing just the characters from '({[]})', determine if
    the input string is valid - that is open brackets are closed by the same
    type of brackets and in correct order.

"""

class Solution:
    def isValid(self, s):
        if not s:
            return False
        bracketMap = {
            ')' : '(',
            '}' : '{',
            ']' : '[]'
        }

        for bracket in s:
            if bracket in '({[':
                stack.append(bracket)
            else:
                if not stack or stack.pop() != bracketMap[bracket]:
                    retrun False
        return not stack

