# 380. Insert, Delete, GetRandom O(1)

Implement the RandomizedSet class.

---

To Implement the RandomizedSet, we require two compoenents: queue and hashmap.
The iterable queue is required to pick the random elements; and hashmap is for
quickly updating the values as they are inserted and deleted.

---

Python:

```python

class RandomizedSet:
    def __init__(self):
        self.q = list()
        self.d = dict()

    def insert(self, val):
        if val in self.d:
            return False
        self.d[val] = len(self.q)
        self.q.append(val)
        return True

    def delete(self, val):
        if val not in self.d:
            return False
        removeIdx, swapVal = self.d[val], self.q[-1]
        self.d[swapVal], self.q[removeIdx] = removeIdx, swapVal
        self.d.pop(val)
        self.q.pop()
        return True

    def getRandom(self):
        return random.choice(self.q)
```
