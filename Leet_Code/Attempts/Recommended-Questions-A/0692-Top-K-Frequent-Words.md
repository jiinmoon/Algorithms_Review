# 692. Top K Frequent Words

 Given a non-empty list of words, return the k most frequent elements.

 Your answer should be sorted by frequency from highest to lowest. If two words
 have the same frequency, then the word with the lower alphabetical order comes
 first.

 ---

 We may first create a count mapping of the each words to its count. Then, we
 could sort by the count to find top K frequent words. Instead of sorting
 entire list, we may use heap to reduce the time complexity to O(log(k) * n).

 ---

 Python:

 ```python

 import heapq
 from collections import Counter

 class Solution:
    def topKFrequentWords(self, words, k):
        counter = Counter(words)
        pq = [(-c, word) for word, c in counter.items()]
        heapify(pq)
        return [heappop(pq)[1] for _ in range(k)]
```
