# 777. Swap Adjacent in LR String

In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move
consists of either replacing one occurrence of "XL" with "LX", or replacing one
occurrence of "RX" with "XR". Given the starting string start and the ending
string end, return True if and only if there exists a sequence of moves to
transform one string to the other.

---

It appears that the questions is geared towards to be approached as a graph
problem of finding the path from the starting string and find its way to the
end string.

The better approach is taking a look at it from the perspective of trying to
balance the number of L swaps to the number of R swaps that needs to occur.

For every char that we explore on the given strings, we find the L characters
can traverse as far left as possible and R characters likewise on the opposite
direction.

If so, then, after counting all the swaps occuring, they both should balance
each other out.

The problem is the case or RL which blocks moving forward or there are more of
L present in start string. These cases will be checked for as we iterate
forward.

Time complexity should be O(n).

---

Python:

```python

class Solution:
    def canTransform(self, start, end):
        if len(start) != len(end) or start == end:
            return start == end

        l, r = 0, 0 # num swaps
        for c1, c2 in zip(start, end):
            # update from start
            l += (c1 == "L")
            r += (c1 == "R")
            
            # swaps are not balanced
            if l != 0 and r != 0:
                return False

            l -= (c2 == "L")
            r -= (c2 == "R")

            # swaps are not balanced or case or RL
            if l > 0 or r < 0 or l != 0 and r != 0:
                return False

        return l == r == 0
```
