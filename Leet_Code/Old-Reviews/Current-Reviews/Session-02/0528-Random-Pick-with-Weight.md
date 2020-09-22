528 Random Pick with Weight
===========================

Given an array of positive integers w. where w[i] describes the weight of ith
index (0-indexed).

We need to call the function pickIndex() which randomly returns an integer in
the range [0, w.length - 1]. pickIndex() should return the integer proportional
to its weight in the w array. For example, for w = [1, 3], the probability of
picking index 0 is 1 / (1 + 3) = 0.25 (i.e 25%) while the probability of
picking index 1 is 3 / (1 + 3) = 0.75 (i.e 75%).

More formally, the probability of picking index i is w[i] / sum(w).

---

Think of this problem as picking a number on a number line - and line is
marked by separators which are separated by its weight. For example, `w = [1,
3]` can be viewed as `[0 --- 1 --- --- --- 4]`.

To do this, we maintain an array of cumulative sums. And when pickIndex is
called, we choose a random integer between 1 and `sum(w[i])`. Now, we find where
this random integer falls within the array we have created using binary search
- the index of where this random value would be inserted is the weighted index.

---

Python:

```python
from random import randint
from bisect import bisect_left

class Solution:
    def __init__(self, w):
        runningSum = 0
        self.cumulativeSums = list()
        for weight in w:
            runningSum += weight
            self.cumulativeSums.append(runningSum)

    def pickIndex(self):
        r = randint(1, self.cumulativeSums[-1])
        return bisect_left(self.cumulativeSums, r)
```


