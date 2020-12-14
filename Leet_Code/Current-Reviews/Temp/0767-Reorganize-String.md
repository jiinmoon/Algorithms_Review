# 767. Reorganize String

Given a string S, check if the letters can be rearranged so that two characters
that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty
string.

---

We are trying to build the longest possible result where two neighbours are not
equal to one another. To do so, we have to arrange the characters such that we
use the most frequent characters first, and then move onto another. To
efficiently track the changing count of the characters, and retrieve the most
frequent character, we can use Max-Heap. Time complexity would be O(n * log(n))
due to n number of heap operations required.

---

Python:

```python

from collections import Counter
from heapq import heappush, heappop, heapify

class Solution767:

    def reorganizeString(self, s):

        # if a character count exceeds half the length, we cannot reorganize
        counter = Counter(s)
        if any(c >= (len(s) + 1) // 2 for c in counter.values()):
            return ""

        # Max-Heap by count of characters
        pq = [(-count, char) for char, count in counter.items()]
        heapify(pq)

        result = []

        def addNewCharacter(char, count):
            result.append(char)
            count -= 1
            if count:
                heappush(pq, (-count, char))

        while pq:

            count, char = heappop(pq)

            if not result or result[-1] != char:
                addNewCharacter(char, -count)

            if not pq:
                return ""
            
            # duplicate ? use the next most frequent character
            count2, char2 = heappop(pq)
            addNewCharacter(char2, -count2)
            heappush(pq, (char, count))

        return "".join(result)
```
