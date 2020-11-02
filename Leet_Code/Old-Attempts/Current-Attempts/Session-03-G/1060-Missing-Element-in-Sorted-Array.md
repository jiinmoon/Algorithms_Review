# 1060 Missing Element in Sorted Array

Maintain the k. From left to right, we take a look at prev and curr values. The
difference between two would be the gap and can be used to determine whether
the k falls within the prev and curr; in which case, we can return k-th next
value from prev.

---

Python:

```python

class Solution:
    def missingElement(self, nums, K):
        nums.append(float('inf'))
        for i in range(1, len(nums)):
            prev, curr = nums[i-1], nums[i]
            gap = curr - prev - 1
            if K - gap <= 0:
                return prev + K
            K -= gap
        return -1
```
