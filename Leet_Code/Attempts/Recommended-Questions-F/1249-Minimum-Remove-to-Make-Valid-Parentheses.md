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

From the given string s, we iterate:

1. Append the opening brackets to our list of open brackets.
2. If a closing bracket encountered, we check to see our "open" bracket list is
   empty, then it is marked for removal. Otherwise, we can pop from the open
   bracket list.

Then, in the end, if any open brackets are left over, it is also added to the
removal.

The time complexity should be O(n) as well as the space complexity.

---

Python:

```python

class Solution:
    def minRemoveToMakeValid(self, s):
        openBrackets = list()
        toRemove = set()
        for i, bracket in enumerate(s):
            if bracket == "(":
                openBrackets.append(i)
            elif bracket == ")":
                # no matching or available open brackets? remove it
                if not openBrackets:
                    toRemove.add(i)
                else:
                    openBrackets.pop()
        # add unmatched open brackets to mark for removal
        toRemove.update(openBrackets)
        return "".join(bracket for i, bracket in enumerate(s) if i not in toRemove)
```
