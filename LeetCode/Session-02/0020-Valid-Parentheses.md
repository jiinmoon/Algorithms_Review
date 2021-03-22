# 20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and
']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

---

As the valid parentheses must be balanced in that every open bracket must be
closed by the matching bracket in order, we can easily check for this condition
using stack. As we encounter open brackets, we push unto the stack. If it is
closing, there should be a matching open bracket on top of the stack. Edge case
here would be unbalanced number of brackets where we would have more open or
closing brackets which should be checked during and after we have finished
iterating on the given input string. The time complexity and space complexity
both be linear.

---

Python:

```python

class Solution20:

    def isValid(self, s):

        m = { ")" : "(", "]" : "[", "}" : "{" }

        stack = []

        for char in stack:

            if char in { "(", "[", "{" }:
                stack.append(char)
            else:
                if not stack or stack.pop() != m[char]:
                    return False

        return not stack
```

