# Maximum Absolute Difference

You are given an array of N integers, A1, A2 ,…, AN. Return maximum value of
f(i, j) for all 1 ≤ i, j ≤ N.

f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value
of x.

---

We simply the given f(i, j) as follows:

```

    f(i,j) = |A[i] - A[j]| + |i - j|

    |A[i] - A[j]| = +/- (A[i] - A[j])
    |i - j| = +/- (i - j)

    Notice that among 4 possibilities, they reduce to two cases.

    Then, we are trying to solve for max(f(i,j)) where 1 <= i < j <= N.

    So, we compute the case for A[i] + i and A[i] - i. Amongst these, we
    compute the maximum differences and find the max in either cases.

```

O(n) in time and space.

---

Python:

```python

class Solution:

    def maxArr(self, arr):

        a, b = [], []

        for i, num in enumerate(arr):
            a.append(num + i)
            b.append(num - i)

        return max(max(a) - min(a), max(b) - min(b))
```
