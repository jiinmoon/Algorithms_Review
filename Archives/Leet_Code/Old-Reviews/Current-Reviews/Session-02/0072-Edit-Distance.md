72 Edit Distance
================

Given two words word1 and word2, find the minimum number of operations required
to convert word1 to word2.

You have the following 3 operations permitted on a word:

```
Insert a character
Delete a character
Replace a character
```

---

We may apply Dynamic Programming here to determine how many edits we need to
perform on the given words. Starting from the end of both words, we move down
until one of the pointer will go below 0. This indicates the base case where
one of the word is empty and we have to delete by the amount of the characters
leftover in other word.

We first check for whether the current words at each pointers match which
indicates that no work is necessary and we can move both pointers safely.

If they do not match, then we have to perform either Insert, Delete, or Replace
operations - and have to find the minimum edit distance required down following
such path.

Since there is a possiblity of overlapping works for each pointers considered,
we should avoid the duplicate work by utilizing the memoization - either use
cache or hashmap structure.

---

Python: using `lru_cache` approach.

```python
from func_tools import lru_cache

class Solution:
    def editDistance(self, word1, word2):
        
        @lru_cache(None)
        def helper(i, j):
            # if either pointer reaches the end, return the length of the other
            # since pointer will go negative, add additional 1 to compensate
            if i < 0 or j < 0:
                return i + 1 + j + 1

            # case:1 current characters under the pointers match
            # no additional work is required, safe to move both pointers
            if word1[i] == word2[j]:
                editDistance = helper(i, j)

            # case:2 if they do not match
            # we have to find the minimum moves required to make them equal
            # perform ins, del, and replace until end
            else:
                editDistance = 1 + min(helper(i-1,j), helper(i,j-1), helper(i-1,j-1))
            return editDistance

        return helper(len(word1)-1, len(word2)-1)
```

