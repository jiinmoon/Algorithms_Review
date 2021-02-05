# 339. Nested List Weighted Sum

Given a nested list of integers, return the sum of all integers in the list
weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be
integers or other lists.

---

We approach this problem with recursion. At each depth, we iterate on every
NestedInteger item. If it is a non-nested integer, we can add to our total.
Otherwise, we have to recurse on itself while increasing the depth to compute
the total to be returned.

The time complexity should be O(n).

---

Python:

```python

class Solution:
    def depthSum(self, nestedList):
        def helper(nestedList, depth=1):
            result = 0
            for curr in nestedList:
                # is non-nested integer
                if curr.isInteger():
                    result += depth * curr.getInteger()
                # is nested, increase depth to compute inwards recursively
                else:
                    result += helper(curr.getList(), depth + 1)
            return result

        return helper(nestedList)
```

