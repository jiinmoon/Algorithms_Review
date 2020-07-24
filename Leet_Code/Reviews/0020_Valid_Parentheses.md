20 Valid Parentheses
====================

Question:
---------

Given a string containing '({[]})', determine whether the string is in valid
format - the parentheses are in order and closed by matching brackets

Solutions:
---------

Whether the "opened" bracket is closed by the correct matching bracket is best
determined with the stack data structure where LIFO opreations allows to look
back at the top of the stack to quickly see whether current "closed" bracket
has a matching "opened" bracket that was pushed onto the stack previously. This
would be O(n) time complexity.

Codes:
------

Python:

```python
class Solution:
    def isValid(self, s):
        parenMap = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        stack = []
        for paren in s:
            if paren in { "(", "[", "{" }:
                stack.append(paren)
            else:
                if not stack or stack.pop() != parenMap[paren]:
                    return False
        return not stack
```

---

**Source:**

LeetCode: [Valid-Parentheses](https://leetcode.com/problems/valid-parentheses/)
