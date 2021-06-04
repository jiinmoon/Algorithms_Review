# 70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you
climb to the top?

---

You can compute this problem by simulating the steps by maintaining previous
values - current step value would be based on previous step values of climbing
either 1 or 2 steps.

---

Python:

```python

class Solution70:

    def climbingStairs(self, n):

        if n < 3:
            return n

        prev, curr = 1, 2
        for i in range(3, n + 1):
            prev, curr = curr, curr + prev

        return curr
```
