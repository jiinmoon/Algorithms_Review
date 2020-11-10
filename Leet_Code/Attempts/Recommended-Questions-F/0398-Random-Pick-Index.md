# 398. Random Pick Index

Given an array of integers with possible duplicates, randomly output the index
of a given target number. You can assume that the given target number must
exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will
not pass the judge.

---

Simplest solution would be to create a hashmap to record each num and its
corresponding indicies. When we require to pick the random index, we first
retrieve the list of indicies in O(1) from the record, and then randomly pick
the index. The process of picking the random index can be O(n) in both time and
space complexity.

---

Python:

```python

from random import choice

class Solution:
    def __init__(self, nums):
        self.d = collections.defaultdict(list)
        for i, num in enumerate(nums):
            self.d[num].append(i)

    def pick(self, target):
        return choice(self.d[target])
```
