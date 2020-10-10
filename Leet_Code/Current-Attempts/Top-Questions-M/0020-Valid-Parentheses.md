# 20 Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and
']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

---

To determine whether given string is valid, we can use the LIFO nature of stack
data structure to confirm our string. Simply, when we encouter open paren, push
onto the stack; otherwise, the matching open paren should be found in the
stack.

---

Python:

```python

class Solution:
    def isValid(self, s):
        stk = list()
        d = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for paren in s:
            if paren in { "(", "[", "{" }:
                stk.append(paren)
            else:
                if not stk or stk.pop() != d[paren]:
                    return False

        return not stk
```
