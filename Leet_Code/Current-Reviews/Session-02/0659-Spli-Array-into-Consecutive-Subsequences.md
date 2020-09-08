659 Split Array into Consecutive Subsequences
=============================================

Given an array nums sorted in ascending order, return True iff you can split it
into 1 or more subsequences such that each subsequence consists of consecurive
integers and has length at least 3.

---

The idea is to use a Counter of each num and its occurrence, and maintain
a record of the subsequences which ends in a particular number.

For example, we have following array:

    [1,2,3,4,5]

Then, we can have a counter where

    {1:1, 2:1, 3:2, 4:1, 5:1}

This allows us to check for whether the number that we are currently on has
been used to build the subsequences. If it is not possible to build such
subsequences (i.e. `[1,2,3,4,4,5]`) then we should fail.

The building process would be as follows:

Iterate on the given array; if the current number count is 0, this indicates
that the all of its number has been used to build the other subsequences
- which means that we can simply continue.

Else, we decrement the counter then check to see whether we have a consecutive
subsequence that has ended just prior to current number (num-1) to see if it
can be extended to include current number as well.

If it does not, then this indicates start of a new subsequence. There has to be
num+1, and num+2 exist within the counter record as well and record it in the
record of subsequences.

If we cannot extend nor create a new subsequences, then we conclude that this
cannot be done and return False.

---

Python:

```python
class Solution:
    def isPossible(self, nums):
        # tracks available number of elements
        f = collections.Counter(nums)
        # records number of subsequences ending on each element
        subSeq = collections.defaultdict(int)

        for num in nums:
            if not f[num]: continue
            f[num] -= 1

            # can we extend from previous subsequence?
            if subSeq[num - 1]:
                subSeq[num - 1] -= 1
                subSeq[num] += 1

            # can we create a new subSequence [num, num+1, num+2]?
            elif f[num + 1] and f[num + 2]:
                f[num + 1] -= 1
                f[num + 2] -= 1
                subSeq[num + 2] += 1

            # cannot extend nor make new subsequence
            else:
                return False

        return True
```



