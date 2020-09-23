# 528 Random Pick with Weight

Use binary search on the cumulative weights to find the index to scale with the
weights.

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

    def pickRandom(self):
        i = random.randint(1, self.weights[-1])
        return bisect.bisect_left(self.weights, i)
```
