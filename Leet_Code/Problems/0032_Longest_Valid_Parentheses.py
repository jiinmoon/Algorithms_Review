""" 32. Longest Valid Parentheses

Question:

    Given a string containing just the characters '()', find the length of the
    longest valid parentheses substring.

+++

Solution:

    Just as we used the stack to confirm valid parentheses, we may use the stack
    to our advantage - but here, we use indicies of the parenthesis that we
    encounter. As we iterate, this effectively cancels out the indicies of valid
    segments - leaving behind only the indicies where the valid segment is
    broken up. Thus, this can be used to calculate the length of the each valid
    segments.

"""

class Solution:
    def longestValidParentheses(self, s):
        stack = []
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    stack.append(i)

        longest = 0
        if stack:
            i = len(s)
            while stack:
                j = stack.pop()
                longest = max(longest, i - j - 1)
                i = j
            longest = max(longest, i)
        else:
            longest = len(s)
        return longest
