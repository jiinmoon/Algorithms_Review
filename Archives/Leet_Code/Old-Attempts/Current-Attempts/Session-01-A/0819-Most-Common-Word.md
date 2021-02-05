# 819 Most Common Word

Use regex to isolate the words, and count each found words which are not found
in the set of banned words.

---

Python:

```python

import re

class Solution:
    def mostCommonWord(self, s, banned):
        s = re.sub("[^A-Za-z0-9]", " ", s)
        banned = set(banned)
        banned.add("")

        counter = collections.defaultdict(int)
        for word in s.split(" ").lower():
            if word not in banned:
                counter[word] += 1

        return max(counter.items(), key = lambda x : x[1])[0]
```
