# 55. Jump Game

Given an array of non-negative integers, you are initially positioned at the
first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

---

Starting from the behind, we maintain the current position which is the maximum
reachable position. Iterating from right to left, we update the current
position if current position can be overtaken by current index + nums[index].
In the end, check whether the current position has reached the starting
position of 0.

---

Python:

```python

class Solution:
    def jumpGame(self, nums):
        m = len(nums)
        currPos = m - 1
        for i in range(m-1, -1, -1):
            if i + nums[i] >= currPos:
                currPos = i
        return not currPos
```
