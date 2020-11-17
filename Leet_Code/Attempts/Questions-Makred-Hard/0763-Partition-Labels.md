# 763. Partition Labels

A string S of lowercase English letters is given. We want to partition this
string into as many parts as possible so that each letter appears in at most
one part, and return a list of integers representing the size of these parts.

---

The focus here should be the partition strategy used - simply put, this is
about finding out where the each unique character "last" appears in the given
string. Partition occurs whenever we found the current character is at its last
position. Then, we should maintain current partition's starting and ending
positions such that we can mark and record them.

Firstable, we should create a hashmap to record the character to its last index
map. Based on this, we iterate forward and checking to see that whether the
current character is at its last position. If so, current partition size is
based on the previous starting position and current ending position.

The time complexity of this algorithm should be O(n) in both time and space
complexity as linear scan is sufficent and requires space to maintain the index
mapping.

---

Python:

```python

class Solution:
    def partition(self, s):
        m = {c:i for i, c in enumerate(s)}
        start, end = 0, 0
        result = list()

        for i, c in enumerate(s):
            # end is updated as far out as possible
            end = max(end, m[c])
            if i == end:
                result.append(end - start + 1)
                start = i + 1

        return result
```
