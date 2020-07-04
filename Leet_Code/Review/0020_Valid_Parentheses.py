""" 20. Valid Parentheses

Question:

    Given the a string containing elements in '({[}])', check whether the given
    string has a well-ordered, well-formed parentheses.

+++

Solution:

    For this problem, we can use stack to leaverge on its LIFO nature. For
    every open parentheses we encounter, we push unto the stack. If closed
    parentheses are found, then its matching open parentheses should be on the
    top of the stack. Since there are three different types of parentheses, we
    need to map this - for this, we will use hashmap structure.

"""

class Solution:
    def validParentheses(self, s):
        if not s or s == '':
            return True
        if len(s) % 2 == 1:
            return False
        stack = []
        mappings = {
            ']' : '[',
            '}' : '{',
            ')' : '('
        }
        for paren in s:
            if paren in {'(', '{', '['}:
                stack.append(paren)
            else:
                if not stack or stack.pop() != mappings[paren]:
                    return False
        return True

