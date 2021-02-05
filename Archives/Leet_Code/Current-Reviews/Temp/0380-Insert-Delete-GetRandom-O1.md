# 380. Insert Delete GetRandom O(1)

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

To support this class, we require two data structures - hashmap and queue. The
combination is required as we need their respective pros.

By using a simple queue (or list), we may insert a value in O(1). But removing
will be a O(n) operation. To resolve this, we require hashmap to quickly
identify the value's membership and remove them in O(1).

This begs the question of why not solely use a hashmap (or set) structure. This
is because to choose a random value, we require subscriptable - or iteratable
structure. To convert our hashmap into a list structure would cost us O(n) for
every getRandom call.

To solve this problem, we use both hashmap and queue. In the hashmap, we store
the value of index where the value is stored. Thus, this will allow us to
quickly remove a value from our list as well. If it is a doubly linked list, we
require no further action, but suppose it is an array. Then we would still need
more time to shift the array if we are to delete from anywhere but tail. So, we
always choose to delete at tail by swapping the value from end of list to index
of the value to be removed.

---

Python:

```python

from random import choice

class Solution380:

    def __init__(self):
        self.q = []
        self.d = {}

    def insert(self, val):
        if val in self.d:
            return False

        self.d[val] = len(self.q)
        self.q.append(val)
        return True

    def remove(self, val):
        if val not in self.d:
            return False

        removeIdx, swapVal = self.d[val], self.q[-1]
        self.d[swapVal], self.q[removeIdx] = removeIdx, swapVal
        del self.d[val]
        self.q.pop()
        return True

    def getRandom(self, val):
        return choice(self.q)
```

