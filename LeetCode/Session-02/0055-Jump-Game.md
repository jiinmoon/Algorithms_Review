# 55. Jump Game

Given an array of non-negative integers nums, you are initially positioned at
the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

---

To determine whether we can reach the last index, we can start from the end
goal and see whether how far we can go back to the starting point. Iterating
from behind, we can compute how far we can reach next position by looking for
current index + value at current index.

Hence, time complexity would be linear as only single pass is required.

---

Python:

```python

class Solution55:

    def canJump(self, nums):

        currPos = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] + i >= currPos:
                currPos = i

        return currPos == 0
```

