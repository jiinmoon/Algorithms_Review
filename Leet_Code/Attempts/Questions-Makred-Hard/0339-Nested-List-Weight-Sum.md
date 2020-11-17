# 339. Nested List Weight Sum

Given a nested list of integers, return the sum of all integers in the list
weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be
integers or other lists.

---

Use recursion to compute the sum of nested weights while tracking the depths
for each recursive call made.

---

Python:

```python

class Solution:
    def weightSum(self, nestedList):
        def helper(nestedList, d=1):
            result = 0
            for curr in nestedList:
                if curr.isInteger():
                    result += d * curr.getInteger()
                else:
                    result += helpre(curr.getList(), d + 1)
            return result

        return helper(nestedList)
```

