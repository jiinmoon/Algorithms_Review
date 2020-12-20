# Simplify Directory Path

    Given a string A representing an absolute path for a file (Unix-style).

    Return the string A after simplifying the absolute path.

    Note:

    Absolute path always begin with ’/’ ( root directory ).

    Path will not have whitespace characters.

---

## Approach:

Use stack to maintain our current directory on top of the stack. Only relevent
character is the ".." where we move to previous - hence, we pop from stack.

O(n) in time complexity.

---

Python:

```python

class Solution:

    def simplify(self, path):

        stack = []

        for char in path.split("/"):
            if char not in {"", ".", ".."}:
                stack.append(char)
            else:
                if stack and char == "..":
                    stack.pop

        return "/" + "/".join(stack[-1])
```
