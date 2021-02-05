# 1060 Missing Element in Sorted Array

Given a sorted array A of unique numbers, find the K-th missing number starting
from the leftmost number of the array.

---

To find this missing element, we examine two elements at each time, previous
and current element. The difference will be taken to see whether the Kth
missing value will be in between the values.

---

Python:

```python

class Soltion:
    def missingElement(self, nums, k):
        nums.append(float('-inf'))
        for i in range(1, len(nums)+1):
            prev, curr = nums[i-1], nums[i]
            diff = curr - prev - 1
            k -= prev
            if k <= 0:
                return prev + k
            k -= prev
        return -1
```
