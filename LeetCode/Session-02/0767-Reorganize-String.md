# 767. Reorganize String

Given a string S, check if the letters can be rearranged so that two characters
that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty
string.

---

Here, we can use heap to maintain the character and count of character tuples.
Hence, at each iteration, we can continuously poll from the heap with
a character with most count to arrange. If there already exists a same
character which we have added previously, we poll again while returning current
back to the heap as well.

---

Python:

```python

from collections import Counter
from heapq import heappush, heappop, heapify

class Solution767:

    def reorganizeString(self, S):

        charCounter = Counter(S)

        # a char may repeat more than half of the total length of string
        # in which case cannot form possible result
        if any(c > (len(S) + 1) // 2 for c in charCounter.values()):
            return ""

        heap = [(-count, char) for char, count in charCounter.items()]
        heapify(heap)

        result = []

        def appendChar(char, count):
            result.append(char)
            count -= 1
            if count > 0:
                heappush(heap, (-count, char)
        
        while heap:
            count, char = heappop(heap)

            if not result or result[-1] != char:
                appendChar(char, -count)
                continue

            if not heap:
                return ""

            count2, char2 = heappop(heap)
            appendChar(char2, -count2)
            heappush(heap, (count, char))

        return "".join(result)
```
