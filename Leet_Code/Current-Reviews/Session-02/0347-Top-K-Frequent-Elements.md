347 Top K Frequent Elements
===========================

Given a non-empty array of integers, return the k most frequent elements.

---

We could count and create tuples of count, element pair and sort. But, more
efficiently, we can use heap to reduce the time complexity as heapify only
costs linear time complexity, and heappop costs log(n) - repeated for O(k
* log(n)). This is better than O(n * log(n)) given k is less than n.

---

Python:

```python

import heapq

class Solution:
    def topKFrequent(self, nums, k):
        counter = collections.Counter(nums)
        # create max heap (negate first val used to compare)
        pq = [(-count, element) for element, count in counter]
        heapify(pq)
        return [heappop(pq)[1] for _ in range(k)]
```
