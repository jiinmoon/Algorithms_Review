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

Java:

```java

import java.util.ArrayList;
import java.util.HashMap;
import java.util.PriorityQueue;

class Solution {
    // HeapItem maintains (word, count)
    static public HeapItem implements Comparable<HeapItem> {
        private String word;
        private int count;

        public HeapItem(String word, int count) {
            this.word = word;
            this.count = count;
        }
        
        @Override
        public int compareTo(HeapItem other) {
            // return first by count
            // if same, return by lexicographically
            return (this.count != other.count) ?
                this.count - other.count :
                other.word.compareTo(this.word);
        }
    }

    public List<String> topKFrequent(String[] words, int k) {
        Map<String, Integer> counter = new HashMap<>();
        for (String word : words)
            counter.put.(word, counter.getOrDefault(word, 0) + 1);

        PriorityQueue<HeapItem> pq = new PriorityQueue<>();
        for (String word : counter.keySet()) {
            pq.add(new HeapItem(word, counter.get(word));
            if (pq.size() > k) pq.remove();
        }

        List<String> result = new ArrayList<String>;
        while (!pq.isEmpty()) result.add(pq.remove().word);

        Collections.reverse(result);

        return result;
    }
}

```

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
