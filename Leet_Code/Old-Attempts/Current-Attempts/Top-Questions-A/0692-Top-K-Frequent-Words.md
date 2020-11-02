# 692 Top K Frequent Words

Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words
have the same frequency, then the word with the lower alphabetical order comes
first.

---

We first count the each of the word in a hashmap structure, then convert it
into tuple of (count, word). Then, when we sort by the count, we can retrieve
the K frequent words. Here, we can make an improvement by using the heap such
that we do not have to sort the entire list.

---

Python:

```python

import heapq

class Solution:
    def topKFrequent(self, words, K):
        counter = collections.Counter(words)
        # negate count for max heap
        pq = [(-count, word) for word, count in counter.items()]
        heapify(pq)
        return [heappop(pq)[1] for _ in range(K)]
```
