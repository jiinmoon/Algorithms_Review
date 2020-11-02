# 45. Jump Game II

Given an array of non-negative integers nums, you are initially positioned at
the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.

---

Here, we perform the jump game ourselves while updating the max jump that can
be performed at each position. If the max jump exceeds the end of the list, we
can return the jump number. Otherwise, we repeat the process.

---

Python:

```python

class Solution:
    def jumpGame(self, nums):
        start, end, maxJump, jumps = 0, 0, 0, 1
        while True:
            for i in range(start, end + 1):
                maxJump = max(maxJump, i + nums[i])
            if maxJump >= len(nums) - 1:
                return jumps
            jumps += 1
            start = end + 1
            end = maxJump
```
