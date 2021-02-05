# 1249. Minimum Remove to Make Valid Parentheses

Given a string s of '(' , ')' and lowercase English characters. 

Your task is to remove the minimum number of parentheses ( '(' or ')', in any
positions ) so that the resulting parentheses string is valid and return any
valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid
strings, or
It can be written as (A), where A is a valid string.

---

Iterate on the given character, and we mark the indicies of the
invalid/unmatched parentheses as determined with a stack. Reconstruct the
result by skipping over the indicies marked for removal.

O(n) in time complexity and space.

---

Python:

```python

class Solution1249:

    def minRemove(self, s):

        stack, remove = list(), set()

        for i, char in enumerate(s):
            
            if char == "(":
                stack.append(char)
            elif char == ")":
                if not stack:
                    remove.add(i)
                else:
                    stack.pop()

        # any remaining open parentheses are to be removed
        remove.update(stack)

        return "".join(c for i, c in enumerate(s) if i not in remove)
```
