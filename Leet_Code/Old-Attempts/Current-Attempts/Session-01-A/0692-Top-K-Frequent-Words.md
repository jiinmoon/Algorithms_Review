# 692 Top K Frequent Words

First, count the frequency of each words and use heap to remove the K frequent
words.

---

Python:

```python

import heapq

class Solution:
    def kFrequentWords(self, words, K):
        counter = collections.Counter(words)
        pq = [(-c, word) for word, c in counter.items()]
        heapify(pq)
        return [heappop(pq)[1] for _ in range(K)]
```
