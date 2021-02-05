# 767. Reorganize String

Given a string S, check if the letters can be rearranged so that two characters
that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty
string.

---

To build the result, we need to build up the string from the character that has
the largest count first and alternate. Since at each stage we need a way to
extract the character with largest count, we first create the count mapping and
then convert into the max heap.

---

Python:

```python

import heapq

class Solution:
    def reorganizeString(self, s):
        def helper(char, count):
            result.append(char)
            count -= 1
            if count:
                heappush(pq, (-count, char))

        counter = collections.Counter(s)
        if any(c >= (len(s) + 1) // 2 for c in counter.values()):
            return ""

        pq = [(-count, char) for char, count in counter.items()]
        heapify(pq)

        result = list()
        while pq:
            count, char = heappop(pq)
            if not result or result[-1] != char:
                helper(char, -count)
            if not pq:
                return ""
            count2, char2 = heappop(pq)
            helper(char2, -count2)
            heappush(pq, (count, char))

        return "".join(result)
```
