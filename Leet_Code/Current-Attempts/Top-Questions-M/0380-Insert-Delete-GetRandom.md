# 380 Insert Delete GetRandom O(1)

Implement the RandomizedSet class:

```
bool insert(int val) Inserts an item val into the set if not present. Returns
true if the item was not present, false otherwise.

bool remove(int val) Removes an item val from the set if present. Returns true
if the item was present, false otherwise.

int getRandom() Returns a random element from the current set of elements (it's
guaranteed that at least one element exists when this method is called). Each
element must have the same probability of being returned.
```

Follow up: Could you implement the functions of the class with each function
works in average O(1) time?

---

Implementing a simple set involves a hashmap structure; but the problem is that
we need an iterable structure to be able to select a random index out of the
list of the values stored. Thus, to support both aspect, we require two
separate structures: we require hashmap to easily store and remove values; and
queue for selecting the random value.

To support updating the values in average O(1) with queue, for each value in
hashmap, we pair it with index of the values' position in the queue. Thus, when
a value is removed, we can quickly identify which value to remove from the
queue as well.

---

Python:

```python

from random import choice

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

    def remove(self, val):
        if val in self.d:
            removedIdx, lastVal = self.d[val], self.q[-1]
            self.d[val] = removedIdx
            self.q[removedIdx] = lastVal
            self.d.pop(val)
            self.q.pop()
            return True
        return False

    def getRandom(self):
        return choice(self.q)
```
