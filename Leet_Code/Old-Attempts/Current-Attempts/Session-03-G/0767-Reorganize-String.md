# 767 Reorganize String

Use heap to maintain the counts of each characters; starting from the most, we
append chars.

---

Python:

```python

import heapq

class Solution:
    def reorganize(self, s):
        def addChar(char, count):
            res.append(char)
            count -= 1
            if not count:
                heappush(pq, (-count, char))

        counter = collections.Counter(s)
        if any(c >= (len(s) + 1) // 2 for c in counter.values()):
            return ""

        pq = [(-c, char) for char, c in counter.items()]
        heapify(pq)

        res = list()
        while pq:
            count, char = heappop(pq)
            if not res or res[-1] != char:
                addChar(char, -count)
                continue
            if not pq:
                return ""
            count2, char2 = heappop(pq)
            addChar(char2, -count2)
            heappush(pq, (count, char))

        return "".join(res)
```
