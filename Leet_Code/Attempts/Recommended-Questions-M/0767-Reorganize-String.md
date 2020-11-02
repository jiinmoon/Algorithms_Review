# 767. Reorganize String

Given a string S, check if the letters can be rearranged so that two characters
that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty
string.

---

To create a new string where none of the two same letters are adjacent to each
other, we need to identify the count of each of the characters; and to
rearrange as far out as possible, we need to use the characters which has
a highest count first then move onto the next. To allow for this, we use heap
to maintain the maximum count word on top of the heap. Since we are reducing
the size of the character pool as we build on the new string, the time
complexity should be of O(n * log(k)) where k is the count of the characters
which we costs us for each time we update the heap.

---

Python:

```python

import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s):
        def addChar(char, count):
            result.append(char)
            count -= 1
            if count:
                heappush(pq, (-count, char))

        counter = Counter(s)
        if any(c >= (len(s) + 1) for c in counter.values()):
            return ""
        
        # create a max heap based on count of each character
        pq = [(-c, char) for char, c in counter.items()]
        heapify(pq)

        result = list()
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
