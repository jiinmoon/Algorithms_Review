# 659 Split Array into Consecutive Subsequences

Given an array nums sorted in ascending order, return true if and only if you
can split it into 1 or more subsequences such that each subsequence consists of
consecutive integers and has length at least 3.

---

For this problem, we first take the list of integers and create a frequency map
of each integer to its frequncy using hashmap structure. Then, we create an
indicator of count of each subsequence ending in a particular integer.

So, the idea is to iterate on the every integer. If we can find the previous
continuation of the current integer (integer - 1) within the subsequence
indicator map, then we know that current value will extend - we record as such.
Else, the previous subsequence is broken, and we need to consider next
subsequence - but to do so, we need to check for next integer +1 and +2 value
since the length has to be "at least 3".

---

Python:

```python

from collections import Counter, defaultdict

class Solution:
    def isPossible(self, nums):
        counter = Counter(nums)
        subseq = defaultdict(int)

        for num in nums:
            if not counter[num]:
                continue
            counter[num] -= 1
            
            if subseq[num-1]:
                subseq[num-1] -= 1
                subseq[num] += 1
            elif counter[num+1] and counter[num+2]:
                counter[num+1] -= 1
                counter[num+2] -= 1
                subseq[num+2] += 1
            else:
                return False

        return True
```
