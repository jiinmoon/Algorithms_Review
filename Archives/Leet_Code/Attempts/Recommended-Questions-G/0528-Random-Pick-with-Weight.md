# 528. Random Pick with Weight

You are given an array of positive integers w where w[i] describes the weight
of ith index (0-indexed).

We need to call the function pickIndex() which randomly returns an integer in
the range [0, w.length - 1]. pickIndex() should return the integer proportional
to its weight in the w array. For example, for w = [1, 3], the probability of
picking the index 0 is 1 / (1 + 3) = 0.25 (i.e 25%) while the probability of
picking the index 1 is 3 / (1 + 3) = 0.75 (i.e 75%).

More formally, the probability of picking index i is w[i] / sum(w).

---

We visualize this problem as a picking an index of from a scaled number line
- thus, we prepare a scaled number line by first creating a list of cumulative
  weights in the constructor. Then, it is a matter of picking the randomized
  weighted value from 1 to last value in the weighted list; then find the index
  of the value with binary search algorithm.

---

Python:

```python

from bisect import bisect_left
from random import randint

class RandomWeightPicker:
    def __init__(self, weights):
        self.q = list()
        temp = 0
        for weight in weights:
            temp += weight
            self.q.append(temp)

    def pickIndex(self):
        i = randint(1, self.q[-1])
        return bisect_left(self.q, i)
```
