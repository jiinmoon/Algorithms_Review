# 78. Subsets

Given an integer array nums of unique elements, return all possible subsets
(the power set).

The solution set must not contain duplicate subsets. Return the solution in any
order.

---

To generate all power set of the given elements, we start from empty set, and
continuously append element to all sets as we build them up. The time
complexity would be based on the number of power set to generate.

---

Python:

```python

class Solution78:

    def subsets(self, nums):

        result = [[]]
        
        for num in nums:
            m = len(result)
            for i in range(m):
                result.append(result[i] + [num])

        return result
```
