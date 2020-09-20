403 Frog Jump
=============

A frog is crossing a river that is divided into x units and at each unit there
may or may not exist a stone. The frog can jump on a stone, but it must not
jump into the water.

Given a list of stone's positions in osrted asending order, determine if the
frog is able to cross the river by landing on the last stone. Initially, the
frong is on the first stone and assume the first jump must be 1 unit.

If the frog's last jump was k units, then its next jump must be either k-1,
k or k+1 units. Note that frog can only jump in the forward direction.

---

We approach this problem by maintain a set of previous jump distances where it
can reach the current stone; so we create a hashmap where key is the current
stone position, and value is set of all jump distances that may reach that
stone.

Starting from each stone, we find the previous jump distances stored in this
hashmap; then perform all possible moves (prev-jump-dist +1, -1, +0). If this
can reach, we update the hashmap.

Since we are computing all possible jumps for each stone positions, the time
complexity is bounded by O(n^2).

---

Python:

```python

class Solution:
    def canCross(self, stones):
        prevJumpDists = { stone: set() for stone in stones }
        prevJumpDists[0].add(0) # initial startin condition
        
        for stone in stones:
            for prevJump in prevJumpDists[stone]:
                for nextJump in [prevJump+i for i in (-1, 0, 1)]:
                    # if the next possible move is able to reach forward stone
                    if nextJump > 0 and stone + nextJump in prevJumpDists:
                        # update the reached stone and it prevJumpDists
                        prevJumpDists[stone + nextJump].add(nextJump)
        
        # the set should not be empty if can cross
        return prevJumpDists[stones[-1]]
```

