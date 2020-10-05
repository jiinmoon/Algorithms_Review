# 528 Random Pick with Weight

You are given an array of positive integers w where w[i] describes the weight
of ith index (0-indexed).

We need to call the function pickIndex() which randomly returns an integer in
the range [0, w.length - 1]. pickIndex() should return the integer proportional
to its weight in the w array. For example, for w = [1, 3], the probability of
picking the index 0 is 1 / (1 + 3) = 0.25 (i.e 25%) while the probability of
picking the index 1 is 3 / (1 + 3) = 0.75 (i.e 75%).

More formally, the probability of picking index i is w[i] / sum(w).

---

To create a randomized pick that support the percentage weights, we think of
this problem as a picking a number on a number line where each index is scaled
by the weights. To do this, we create a list of cumulative prefix sum of the
weights, then when we pick the random value, we perform binary search of the
randomize value between 1 to cumulative sum of all the weights. That insertion
point should be the weighted pick.

---

Python:

```python

class RandomWeight:
    def __init__(self, weights):
        self.weights = list()
        temp = 0
        for w in weights:
            temp += w
            self.weights.append(temp)
    
    def pick(self):
        i = random.randint(1, self.weights[-1])
        return bisect.bisect_left(self.weights, i)
```
