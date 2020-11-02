# 767 Reorganize Strings

Given a string S, check if the letters can be rearranged so that two characters
that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty
string.

---

To rearrange the given string such that two adjacent characters unique, the
simplest method is to continuously expand the characters of highest frequency
first. To enable this, we first count the frequency of the each characters; we
can easily detect whether the given string is "rearrange-able" by first
checking the counts - if any single char has more than "half" of the frequency,
we cannot possibly complete the process.

Then, we create a max heap - this will allow us to quickly select for the
character that has the highest count in efficient manner (log(n) in insertion
and removal). Until we exhaust our pool, we continouly append and update the
heap.

---

Python:

```python

import heapq
from collections import Counter

class Solution:
    def reorganize(self, s):
        def addChar(char, count):
            result.append(char)
            count -= 1
            if count:
                heappush(pq, (-count, char))

        counter = Counter(s)
        if any(count >= (len(s)+1) for count in counter.values()):
            return ""

        pq = [(-count,char) for char, count in counter.items()]
        heapify = pq
        result = []

        while pq:
            count, char = heappop(pq)
            if not result or result[-1] != char:
                addChar(char, -count)
            if not pq:
                return ""
            count2, char2 = heappop(pq)
            addChar(char2, -count2)
            heappush(pq, (count, char))

        return "".join(result)
```
