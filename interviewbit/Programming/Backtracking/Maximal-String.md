# Maximal String

    Given a string A and integer B, what is maximal lexicographical string that
    can be made from A if you do atmost B swaps.

---

## Approach:

Use backtrack to explore all possible swaps that can generate the greater value
at each recursion depth. When all swaps are performed, we return.

O(B * n^2) in time complexity as for B number of swaps, we have to perform
search for swap positions that can generate maximal string.

---

Python:

```python

class Solution:

    def maximalString(self, A, B):

        if not B:
            return A

        def helper(path, k):
            nonlocal result

            if not k:
                return
            
            # find swap position where we push greater value to left
            for i in range(len(A)-1):
                for j in range(i+1, len(A)):

                    if path[j] > path[i]:
                        path[j], path[i] = path[i], path[j] 

                        # record possible maximum
                        if result < path:
                            result = path[:]

                        # recurse until k == 0
                        helper(path, k - 1)

                        # restore path for next backtrack
                        path[j], path[i] = path[i], path[j] 
        
        result = list(A)
        helper(list(A), B)

        return "".join(result)
```
