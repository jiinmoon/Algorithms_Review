# 460 LFU Cache

Design and implement a data structure for Least Frequently Used (LFU) cache.

Implement the LFUCache class:

```
LFUCache(int capacity) Initializes the object with the capacity of the data
structure.

int get(int key) Gets the value of the key if the key exists in the cache.
Otherwise, returns -1.

void put(int key, int value) Sets or inserts the value if the key is not
already present. When the cache reaches its capacity, it should invalidate the
least frequently used item before inserting a new item. For this problem, when
there is a tie (i.e., two or more keys with the same frequency), the least
recently used key would be evicted.
```

Notice that the number of times an item is used is the number of calls to the
get and put functions for that item since it was inserted. This number is set
to zero when the item is removed.

Follow up:

Could you do both operations in O(1) time complexity?

---

To implement this class, we require not only the frequency counter but also the
time that the items were last used - this is to invalidate the items that
shares the same frequency. To find the LFU item, priority queue can be used to
keep track of the items key, frequency and time. To achieve O(1) in time
complexity, we cannot simply update the pq everytime. Instead, we opt to update
the pq only when it is necessary - that is when we have to invalidate and
determine the LFU item from the pq. To do so, we maintain a sepatate frequency
and time mapping as well as the set of keys that has been marked for update. So
when we perform update, we can look at the update set to update the necessary
items in the pq.

---

Java:

```java

import java.util.HashMap;
import java.util.HashSet;
import java.util.PriorityQueue;

class LFUCache {
    
    static class Triplet implements Comparable<Triplet> {
        private int time, frequency, key;

        public Triplet(int time, int frequency, int key) {
            this.time = time;
            this.frequency = freqeuency;
            this.key = key;
        }
        
        @Override
        public int compareTo(Triplet other) {
            // compare first by frequency then time
            int cmp = Integer.compare(this.frequency, other.frequency)
            return (cmp != 0) cmp : Integer.compare(this.time, other.time)
        }
    }
    
    private int capacity, time;
    private HashMap<Integer, Integer> map;
    private HashMap<Integer, List<Integer>> freqTimeMap;
    private Set<Integer> updateKeySet;
    private PriorityQueue<Triplet> pq;

    public LFUCache(int capacity) {
        this.capacity = capacity;
        this.time = 0;
        this.map = new HashMap<>();
        this.freqTimeMap = new HashMap<>();
        this.updateKeySet = new HashSet<>();
        this.pq = new PriorityQueue<>();
    }

    public int get(int key) {
        if (!this.map.containsKey(key)) return -1; 

        this.time++;
        List<Integer> freq_time = this.freqTimeMap.get(key);
        this.freqTimeMap.put(key, List.of(freq_time.get(0), this.time));
        this.updateKeySet.add(key);
        return this.map.get(key);
    }
    
    public void put(int key, int value) {
        if (this.capacity <= 0)
            return -1;

        this.time++;
        if (this.map.containsKey(key)) {
            get(key);
        } else {
            if (this.capacity == this.map.size()) {
                while (!this.pq.isEmpty() && this.updateKeySet.contains(this.pq.peek().key)) {
                    int updateKey = this.pq.remove().key;
                    List<Integer> freqTime = this.freqTimeMap.get(updateKey);
                    this.pq.add(new Triplet(freqTime.get(0), freqTime.get(1), updateKey));
                    this.updateKeySet.remove(updateKey);
                }
                int removeKey = pq.remove().key;
                this.freqTimeMap.remove(removeKey);
                this.amp.remove(removeKey);
            }
            this.freqTimeMap.put(key, List.of(0, this.time));
            this.pq.add(new Triplet(0, this.time, key));
        }
        this.map.put(key, value);
    }
}


```

Python:

```python

import heapq

class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.time = 0
        self.d, self.ft = dict(), dict()
        self.pq, self.update = list(), set()
    
    def get(self, key):
        self.time += 1
        if key not in self.d:
            return -1
        f, _ = self.ft[key]
        self.ft[key] = (f + 1, self.time)
        self.update.add(key)
        return self.d[key]

    def put(self, key, val):
        self.time += 1
        if key in self.d:
            f, _ = self.ft[key]
            self.ft[key] = (f + 1, self.time)
            self.update.add(key)
        else:
            if self.capacity == len(self.d):
                while self.pq and self.pq[0][2] in self.update:
                    _, _, updateKey = heappop(pq)
                    f, t = self.ft[updateKey]
                    heappush(pq, (f, t, updateKey))
                    self.update.remove(updateKey)
                _, _, removeKey = heappop(pq)
                self.ft.pop(removeKey)
                self.d.pop(removeKey)
            self.ft[key] = (0, self.time)
            heappush(pq, (0, self.time, key))
        self.d[key] = val
```

