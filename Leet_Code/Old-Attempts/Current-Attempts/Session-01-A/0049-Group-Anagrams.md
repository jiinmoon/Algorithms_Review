# 49 Group Anagrams

Use hashmap to store sorted key : list of word that have the same anagrams.

---

Python:

```python

class Solution:
    def groupAnagrams(self, words):
        d = collections.defaultdict(list)
        for word in words:
            d[tuple(sorted(word))].append(word)

        return d.values()
```
