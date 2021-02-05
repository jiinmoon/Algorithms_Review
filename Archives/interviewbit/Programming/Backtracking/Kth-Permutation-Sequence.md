# Kth Permutation Sequence

    The set [1,2,3,…,n] contains a total of n! unique permutations.

    By listing and labeling all of the permutations in order,
    We get the following sequence (ie, for n = 3 ) :

    1. "123"
    2. "132"
    3. "213"
    4. "231"
    5. "312"
    6. "321"

    Given n and k, return the kth permutation sequence.

---

## Approach:

Here, trick is to realize that the kth permutation sequence is "fixed" so to
speak. From candidates [1, 2, 3, ..., n], each choice of the candidates for
every possible positions are fixed by given k. There are n! possibilities,
hence, current position from the candidates can be computed by modulo
operation to determine how many n! steps to move in given k.

---

Python:

```python

from math import factorial

class Solution:

    def kthPermutation(self, n, k):

        candidates = [str(i) for i in range(1, n + 1)]
        result = ""

        k -= 1

        while n > 0:
            index, k = divmod(k, factorial(n))
            result += candidates.pop(index)

        return result
```
