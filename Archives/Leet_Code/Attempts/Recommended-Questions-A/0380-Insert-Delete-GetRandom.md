# 380. Insert, Delete, GetRandom O(1)

Implement the RandomizedSet class.

---

To Implement the RandomizedSet, we require two compoenents: queue and hashmap.
The iterable queue is required to pick the random elements; and hashmap is for
quickly updating the values as they are inserted and deleted.

---

Java:

```java

import java.util.HashMap;
import java.util.LinkedList;
import java.util.Random;

class RandomizedSet {
    private LinkedList<Integer, Integer> list;
    private Map map;
    private static Random rand;

    public RandomizedSet() {
        this.list = new LinkedList<>();
        this.map = new HashMap<>();
        this.rand = new Random();
    }

    public boolean insert(int val) {
        if (this.map.containsKey(val)) return false;
        this.map.put(val, this.list.size());
        this.list.add(val);
        return true;
    }

    public boolean remove(int val) {
        if (!this.map.containsKey(val)) return false;
        int removeIdx = this.map.get(val);
        int swapVal = this.list.get(this.list.size()-1);
        this.map.put(swapVal, removeIdx);
        this.list.add(removeIdx, swapVal);
        this.list.removeLast();
        return true;
    }

    public int getRandom() {
        return this.queue.get(this.rand.nextInt(this.list.size()));
    }
}

```

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
