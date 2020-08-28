767 Reorganize String
=====================

Given a string S, check if the letters can be rearranged so that two characters
that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty
string.

---

The trick is in the frequency of the each characters apperaing in the string.
We can avoid having same two chars next to one another if we rebuild the string
by its frequency and rotate the characters out while decrementing the
characters counts. We can maintain the (counts, char) tuple in the max heap.

The overall time complexity would be O(n * log(k)) where k is the number of
unique characters in the given string to perform heappop operation.

---

Python:

```python
from collection import Counter
from heapaq import heapify, heappop, heappush

class Solution:
    def reorganizeString(self, s):
        charCount = Counter(s)
        # if any one of the characters appear too frequent, we cannot solve.
        # i.e. "aaaab"; here, a appears more than half of the string.
        if any( count > (len(s) + 1) // 2 for count in charCount.values() ):
            return ""

        # convert to max-heap
        heap = [ (-count, char) for char, count in charCount ]
        heapify(heap)

        res = []

        def appendChar(char, count):
            res.append(char)
            count -= 1
            # still count left? push back to heap
            if count:
                heap.append( (-count, char) )

        while heap:
            count, char = heappop(heap)
            
            if not res or res[-1] != char:
                appendChar(char, -count)
                continue

            # if current most frequent char is already in res
            # we need to find next frequent char
            if not heap:
                return ""       # cannot complete
            
            # append next most frequent char
            otherCount, otherChar = heappop(heap)
            appendChar(otherChar, -otherCount)
            # push back current char that we could not use to append
            heappush( (-count, char) )
        
        return "".join(res)
```
