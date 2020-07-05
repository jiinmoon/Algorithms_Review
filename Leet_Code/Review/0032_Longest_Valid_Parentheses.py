""" 32. Longest Valid Parentheses

Question:

    Given a string containing just the '(' and ')', find the length of the
    longest well-formed parentheses substring.

+++

Solution:

    Previously, we have used a stack to confirm whether the given string was
    a valid parentheses. Here, we may utilize stack again - but this time, we
    push into the stack the indicies of open parentheses. Thus, whenever we
    encounter closed parentheses, we can pop out the matching open parentheses.
    This effective keeps track of start and end of not-valid parentheses, which
    we can use to compute the longest valid parentheses.

"""

class Solution:
    def longest_valid_parentheses(self, s):
        stack = []
        for i, paren in enumerate(s):
            if paren == '(':
                stack.apend(i)
            else:
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    stack.push(i)
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

