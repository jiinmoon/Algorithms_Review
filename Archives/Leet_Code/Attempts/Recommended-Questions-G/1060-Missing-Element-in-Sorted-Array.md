# 1060. Missing Element in Sorted Array

Given a sorted array A of unique numbers, find the K-th missing number starting
from the leftmost number of the array.

---

We iterate on the given sorted array comparing the value of previous and
current element. The missing count should be current value minus the previous
value. If ths missing element is found, k - missing count should be below 0; in
which case we can return the previous element + k amount. k at each iteration
is update by - missing count.

---

Python:

```python

class Solution:
    def missingElement(self, nums, k):
        nums.append(float('inf'))
        for i in range(1, len(nums) + 1):
            prev, curr = nums[i-1], nums[i]
            missingCount = curr - prev - 1
            if k - missingCount <= 0:
                return prev + k
            k -= missingCount
        return -1
```
