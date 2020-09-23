# 380 Insert Delete GetRandom

To support picking the randomized element we require a queue like structure.
And to support the insert and delete in constant time, we need a hashmap. So,
on the hashmap we insert value : index pair where index is the position on the
queue. When we need to remove, we replace the removed value's index on the
queue with the last element in the queue.

---

Python:

```python

class RandomizedSet:
    def __init__(self):
        self.q = list()
        self.d = dict()

    def insert(self, val):
        if val not in self.d:
            self.d[val] = len(self.q)
            self.q.append(val)
            return True
        return False

    def delete(self, val):
        if val in self.d:
            removedIdx, lastVal = self.d[val], self.q[-1]
            self.d[lastVal], self.q[removedIdx] = removedIdx, lastVal
            self.d.pop(val)
            self.q.pop()
            return True
        return False

    def getRandom(self):
        return random.choice(self.q)
```
