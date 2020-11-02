# 1296 Divide Array in Sets of K Consecutive Numbers

Given an array of integers nums and a positive integer k, find whether it's
possible to divide this array into sets of k consecutive numbers
Return True if its possible otherwise return False.

---

Best way to divide the array would be to create a frequency map of each of the
numbers present. Then, for each number, we iterate upto number + k to see
whether we can create the set - there has to be enough count of the numbers
present to divide the array into these sets.

---

Python

```python

from collections import Counter

class Solution:
    def isPossible(self, nums, k):
        if not nums or not len(nums) % k: return False
        if k == 1: return True

        counter = Counter(nums)

        for currNum in sorted(counter.keys()):
            currCount = counter[num]
            if not currCount:
                continue

            for nextNum in range(currNum, currNum + k):
                if nextNum not in counter or counter[nextnum] < currCount:
                    return False
                counter[nextNum] -= currCount

        return True
```
