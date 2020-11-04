# 529. Random Pick with Weight

You are given an array of positive integers w where w[i] describes the weight
of ith index (0-indexed).

We need to call the function pickIndex() which randomly returns an integer in
the range [0, w.length - 1]. pickIndex() should return the integer proportional
to its weight in the w array. For example, for w = [1, 3], the probability of
picking the index 0 is 1 / (1 + 3) = 0.25 (i.e 25%) while the probability of
picking the index 1 is 3 / (1 + 3) = 0.75 (i.e 75%).

More formally, the probability of picking index i is w[i] / sum(w).

---

First, create a weighted number line - that is a cumulative weights. Then, we
can randomly select the value from 1 to last cumulative weights and use binary
search algorithm to find the index of the chosen value. The time complexity
should be O(n) for construction and O(log(n)) for choosing random index.

---

Python:

```python

class RandomPick:
    def __init__(self, weights):
        self.weights = list()
        temp = 0
        for weight in weights:
            temp += weight
            self.weights.append(temp)

    def pickIndex(self):
        i = random.randint(1, self.weights[-1])
        return bisect.bisect_left(self.weights, i)
```
