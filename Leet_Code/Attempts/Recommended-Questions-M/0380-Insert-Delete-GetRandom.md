# 380 Insert, Delete, GetRandom O(1)

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

---

To support this RandomizedSet structure, we identify that we require two
components: queue and hashmap. Hashmap is required here to quickly insert and
remove the elements; and a queue is for able to iterate the retrieve the random
element.

To update the queue in O(1) at the same time as the hashmap, we create
a mapping of the element and the its position in the queue on the hashmap.
Thus, if the element needs to be removed, we can identify its position on the
queue quickly, and we can swap it with the last element in the queue and pop.

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

    def remove(self, val):
        if val not in self.d:
            return False
        removeIdx, lastVal = self.d[val], self.q[-1]
        self.d[lastVal], self.q[removeIdx] = removeIdx, lastVal
        self.d.pop(val)
        self.q.pop()
        return True
    
    def getRandom(self):
        return random.choice(self.q)
```
