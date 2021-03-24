# 70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you
climb to the top?

---

The problem is essentially about finding the Fibonacci number where at each
step's result is dependent on the value from previous values.

Naive implementation of such algorithm in recursion can quickly run out of
stack memory as we are deferring the works, generating two additional functions
for each function call, and duplicate works are generated.

There are two solutions to this: one is to implement the recursive algorithm
with memoization technique where we cache the individual function result such
that we can look up without having to recompute the same variables; other is to
implement it in iterative approach.

---

Python:

```python

class Solution70:

    def climb(self, n):

        if n <= 2:
            return n

        prev, curr = 1, 2
        for i in range(3, n + 1):
            prev, curr = curr, prev + curr

        return curr
```
