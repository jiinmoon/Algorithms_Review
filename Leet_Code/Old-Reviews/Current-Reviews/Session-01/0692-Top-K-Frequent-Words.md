692 Top K Frequent Words
========================

Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words
have the same frequency, then the word with the lower alphabetical order comes
first.

---

We first count the words, then convert into tuple of (count, word) such that we
can sort by its first element. We then can sort by the count, but here we can
use heap for more efficiency. Transform the given tuples into heap, then
collect the top k frequent elements.

O(n) time to count the words. O(n) to heapify. O(k log n) to remove top
k elements from heap - so overal complexity is O(n + k * log(n));

---

Python:

```python
from collections import Counter
from heapq import heapify, heappop

class Solution:
    def topKFrequent(self, words, k):
        count = Counter(words)
        # heapq is min heap; negate the count for max heap
        countToWord = [ (-c, w) for w, c in count.items() ]
        # heapify is a constant time, in-place operation
        heapify(countToWord)
        return [heappop(countToWord)[1] for _ in range(k)]
```
