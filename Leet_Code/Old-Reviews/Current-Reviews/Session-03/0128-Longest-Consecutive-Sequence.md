128 Longest Consecutive Sequences
=================================

Given an unsorted array of integers, find the length of the longest consecutive
elements sequence.

---

Simply, we convert the given array into a set - hashmap structure that we can
test for its membership in O(1). Then, for each number in the set, we check
whether we can build as far as possible. We can avoid computing the dulicate
sequences that we have looked previously by ignoring whether num-1 is in the
set - which indicates that it has been computed and included along in previous
iteration.

Time complexity should be O(n).

---

Python:

```python
class Solution:
    def longestConsecutive(self, nums):
        nums = set(nums)
        longest = 0

        for currNum in nums:
            # currNum included in previous iteration
            if currNum-1 in nums:
                continue
            
            nextNum = currNum
            while nextNum in nums:
                nextNum += 1

            longest = max(longest, nextNum - currNum)

        return longest
```
