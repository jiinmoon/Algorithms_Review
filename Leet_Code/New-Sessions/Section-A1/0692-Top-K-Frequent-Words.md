# 692 Top K Frequent Words

Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words
have the same frequency, then the word with the lower alphabetical order comes
first.

---

Firstable, we should create a frequency map of the word to counts such that we
can identify the frequencies of the words easier. Then, we can sort to retrieve
the top K frequently appearing words. Here, we may use heap to avoid having to
sort the entire list, and reduce the time complexity down to O(k * log(n)).

---

Python:

```python

from collections import Counter
import heapq

class Solution:
    def topKWords(self, words, k):
        counter = Counter(words)
        # create max heap; negate the counts
        pq = [(-c, w) for w, c in counter.items()]
        heapify(pq)
        return [heappop(pq)[1] for _ in range(k)]
```
