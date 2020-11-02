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

We require two components to support our RandomizedSet class. Firstable, we
will need a queue or a list structure to be able to randomly select the element
efficiently. Insert and remove can be supported with a hashmap structure. The
problem with using hashmap to getRandom is that retrieving all the elements to
select a random value is going to take O(n).

If we use both queue and hashmap, then we require a way to update the queue
- if we remove the value in the middle of the queue, how can we reflect it as
  fast as possbile? To do so, in the hashmap, we save the value as the key and
  the value's index in the queue as the its value. Hence, when we need to
  remove a value, we can swap that value's position in the queue with the last
  element in the queue.

---

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

    def remove(self, val):
        if val in self.d:
            lastIdx, lastVal = self.d[val], self.q[-1]
            self.d[lastVal], self.q[lastIdx] = lastIdx, lastVal
            self.d.pop(val)
            self.q.pop(val)
            return True
        return False

    def getRandom(self):
        return random.choice(self.q)
```

