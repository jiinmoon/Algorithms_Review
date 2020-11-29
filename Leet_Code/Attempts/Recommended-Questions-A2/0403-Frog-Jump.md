# 403. Frog Jump

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

From each frog position, we create a set of possible next index positions.
Starting from 0, we look at all possible next index to reach (k-1, k, or k+1);
and if it is reachable, we update the set. If we can reach the end after taking
a look at all possible positions and jumps, the set should have been explored.

For each position, we have to examine every possible positions - hence, the
time complexity and space would be O(n^2).

---

Python:

```python

class Solution403:

    def canJump(self, stones):

        d = {stone:set() for stone in stones}
        d[0].add(0)

        for stone in stones:
            for prev in d[stone]:
                for nxt in [(prev+i) for i in (-1, 0, 1)]:
                    if nxt > 0 and stone+nxt in d:
                        d[stone + nxt].add(nxt)
        
        return stones[-1]
```
