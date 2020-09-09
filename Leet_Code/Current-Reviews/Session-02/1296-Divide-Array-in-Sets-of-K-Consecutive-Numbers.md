1296 Divide Array in Sets of K Consecutive Numbers
==================================================

Given an array of integers nums and a positive integer k, find whether it's
possible to divide this array into sets of k consecutive numbers
Return True if its possible otherwise return False.

---

This is exactly the same question as #846 but phrased differently. Here,
instead of heap to simulate building the "straights", we will count each of the
numbers and decrement the count of the other numbers in the straight in range
of upto K.

The time complexity is O(n * log(n)) due to sorting invovled (same as #846 but
there we used heapsort to gurantee picking the minimum ending num to build upon
on each iteration).

---

Python:

```python
from collections import Counter

class Solution:
    def isPossibleToDivide(self, A, K):
        # numbers will remain
        if not A or not K or len(A) % K: return False
        # trivial case
        if K == 1: return True

        counter = Counter(A)

        # from current number as a start position
        # build a straight upto curr + K
        # while updating the count of each numbers used in this way
        for currNum in sorted(counter.keys()):
            if not counter[currNum]: continue
            for nextNum in range(curr, curr + K):
                # not enough num to form groups with current num
                if nextNum not in counter or counter[nextNum] < counter[currNum]:
                    return False
                counter[nextNum] -= counter[currNum]

        return True
```
