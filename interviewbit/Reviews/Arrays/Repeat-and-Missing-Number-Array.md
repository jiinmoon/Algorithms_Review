# Repeat and Missing Number Array

You are given a read only array of n integers from 1 to n.

Each integer appears exactly once except A which appears twice and B which is
missing.

Return A and B.

Note: Your algorithm should have a linear runtime complexity. Could you
implement it without using extra memory?

Note that in your output A should precede B.

---

Let's try to approach this problem mathmatically:

```

For given problem, following statement is true:

    Let Sa be sum of actual given array; Se be sum of expected values from 1 to
    n; m be missing number; and r be repeat number.

        S1:     Se = Sa + m - r
                Se - Sa = m - r

Then, it should also follow then sum of squared elements should hold true:

        S2:     Se^2 - Sa^2 = m^2 - r^2
                Se^2 - Sa^2 = (m + r)(m - r)

We can divide S2 by S1:

        S3:     (Se^2 - Sa^2) / (Se - Sa) = (m + r)(m - r) / (m - r)
                (Se^2 - Sa^2) / (Se - Sa) = m + r

Let P1 to denote (Se^2 - Sa^2) and P2 to denote (Se - Sa); then we can isolate
for m and r as follows:

        S4:     P1 / P2 = m + r
                m = (P1 / P2) - r
                r = (P1 / P2) - m

Substitute the isolated values back to S1 to solve them:

        S5:     P2 = m - r

                P2 = (P1 / P2) - 2r
                r = 0.5 * (P2 - (P1 / P2))

                P2 = 2m - (P1 / P2)
                m = 0.5 * (P2 + (P1 / P2))

```

Hence, we require O(n) time to compute the sums and we can find the missing and
repeat numbers in O(1).

---

Python:

```python

class Solution:

    def repeatedNumber(self, arr):

        n = len(arr) + 1

        Sa = sum(arr)
        Se = sum(i for i in range(1, n))

        SQa = sum(i**2 for i in arr)
        SQe = sum(i**2 for i in range(1, n))

        P1 = SQa - SQe
        P2 = Sa - Se

        m = (P2 + (P1 / P2)) // 2
        r = (P2 - (P1 / P2)) // 2

        return [r, m]
```
