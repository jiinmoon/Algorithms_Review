# 403 Frog Jump

A frog is crossing a river. The river is divided into x units and at each unit
there may or may not exist a stone. The frog can jump on a stone, but it must
not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order,
determine if the frog is able to cross the river by landing on the last stone.
Initially, the frog is on the first stone and assume the first jump must be
1 unit.

If the frog's last jump was k units, then its next jump must be either k - 1,
k, or k + 1 units. Note that the frog can only jump in the forward direction.

---

For this problem, we will compute all the possible jumps from the stone - and
record them to determine the next set of jumps on each of the stones. Hence,
after we have finished the jumps, if we can find any previous jump record on
the last stone, it means that we can complete the task.

---

Python:

```python

class Solution:
    def canCross(self, stones):
        prevJumps = { stone: set() for stone in stones }
        prevJumps[0].add(0)

        for stone in stones:
            for pj in prevJumps[stone]:
                for nj in [(pj+i) for i in (-1, 0, 1)]:
                    if nj > 0 and stone + nj in prevJumps:
                        prevJumps[stone + nj].add(nj)

        return len(prevJumps[stones[-1]]) != 0
```
