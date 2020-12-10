# 78. Subsets

Given an integer array nums, return all possible subsets (the power set).

The solution set must not contain duplicate subsets.

---

We continuously build upon the previous result starting from the empty set, and
expand to add more sets as we take each element into account. The time and
space complexity would be bounded by number of power sets to generate which
there are 2^N of them.

---

Python:

```python

class Solution78:

    def powerset(self, nums):

        result = [ [] ]

        for num in nums:
            m = len(result)
            for i in range(m):
                result.append(result[i] + [num])

        return result
```
