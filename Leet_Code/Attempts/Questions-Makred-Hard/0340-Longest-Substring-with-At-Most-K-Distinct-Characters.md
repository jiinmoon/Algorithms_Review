# 340. Longest Substring with At Most K Distinct Characters

Given a string, find the length of the longest substring T that contains at
most k distinct characters.

---

We approach this problem by using hashmap to record each character that we have
seen so far and its last appearing index.

Thus, this becomes a sliding window problem; we slide forward each time to
consider adding each character to our pool. If we find that size of hashmap
exceeds K, we reduce the beginning of our sliding window. Otherwise, current
marks the potential substring that contains K distinct characters.

The process can complete in O(n) time. The size of sliding window never exceeds
K so space is bounded by O(K).

---

Python:

```python

class Solution:
    def findLongestSubstring(self, s, k):
        record = collections.defaultdict(int)
        start, result = 0, 0

        for end, char in enumerate(s):
            record[char] = end

            while len(record) > k:
                if record[s[start]] == start:
                    record.pop(s[start])
                start += 1
            else:
                result = max(result, end - start + 1)

        return result
```
