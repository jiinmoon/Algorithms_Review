# 659. Split Array into Consecutive Subsequences

Given an array nums sorted in ascending order, return true if and only if you
can split it into 1 or more subsequences such that each subsequence consists of
consecutive integers and has length at least 3.

---

To find whether the given array can be split into subsequences of size 3 that
are consecutive (1, 2, 3...), we first create a count map of the each integers
present. Then, we also maintain a record of the number of subsequences ending
at that integer. Thus, when we iterate on every integer, we can first check to
see whether we have exhasuted all the pool of given integer. If not, then we
check to see this is an extension of the previous consecutive subsequence by
checking the subsequence record of current integer - 1. If so, then we update
the subsequence record. Otherwise, this indicates the beginning of the new
subsequence. Hence, we check to see whether we have enough count of the integer
+1 and +2 then update counter and subsequence record appropriately.

---

Python:

```python

class Solution:
    def splitArray(self, nums):
        subsequences = collections.defaultdict(int)
        counter = collections.Counter(nums)

        for num in nums:
            if not counter[num]:
                continue
            counter[num] -= 1

            if subsequences[num-1]:
                subsequences[num-1] -= 1
                subsequences[num] += 1
            elif counter[num+1] and counter[num+2]:
                counter[num+1] -= 1
                counter[num+2] -= 1
                subsequences[num+2] += 1
            else:
                return False

        return True
```
