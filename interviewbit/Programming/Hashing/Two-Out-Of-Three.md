# Two Out Of Three

    Given are Three arrays A, B and C.

    Return the sorted list of numbers that are present in atleast 2 out of the
    3 arrays.

---

## Approach:

To check whethere the element exist within the two out of three set of numbers,
we simply intersect three sets (A & B), (B & C), (A & C). And union these
elements to find the overlap values.

O(n * log(n)) in time complexity due to sorting involved.

---

Python:

```python

class Solution:

    def solve(self, A, B, C):

        A, B, C = set(A), set(B), set(C)

        result = (A & B) | (B & C) | (A & C)

        return sorted(list(result))
```
