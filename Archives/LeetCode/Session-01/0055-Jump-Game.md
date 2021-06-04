# 55. Jump Game

Given an array of non-negative integers nums, you are initially positioned at
the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

---

We simulate the jump game by recording the maximum position reach-able from
each index by computing current index + maximum jump length at current index.

---

Python:

```python

class Solution55:

    def jumpGame(self, nums):
        
        # starting from end, check whether we can reach 0
        currPos = len(nums) - 1
        for i, num in enumerate(len(nums)-1, -1, -1):
            if nums[i] + i > currPos:
                currPos = i

        return currPos == 0
```
