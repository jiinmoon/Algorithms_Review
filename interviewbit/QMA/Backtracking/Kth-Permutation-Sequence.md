# Kth-Permutation Sequence

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

Suppose that we have a candidates [1, 2, 3, ... n]. Then, as we choose our
number for each position of the permutation sequence, our choices decreases as
well.

For simplicity, let's say we have k of 0. Then, we can choose (n-1)! values for
our first value, and so on for each position following that. This indicates
that number at each position is fixed for K-th permutation sequence (or
pre-determined) which is at (k / (n - 1)! + 1) from our candidates.

Let's try with an example:

```

N = 3, then our candidates are [1, 2, 3]. Suppose K = 4.

To make it zero-indexed, first decrement K by 1.

For first candidate, we can compute its position with above formula:

    3 / (3 - 1)! = 3 / 2 = 1

Hence, our first candidate is [2].

For next candidate, we update our K value with modulo with factorial of n to
wrap around. K becomes 1. As well, we remove the chosen candidate while
decreasing the choice of n as well by 1.

For second candidate,

    1 / (1)! = 1

Hence, our second candidate is [3]. So far, we have [ 2, 3 ]. After final step,
we have our permutation of [ 2, 3, 1]

```

O(n^2) in time complexity due to while choosing the candidates, we also have to
remove the candidate from the list as well.

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
            n -= 1
            idx, k = divmod(k, factorial(n))
            result += candidates.pop(idx)

        return result
```
