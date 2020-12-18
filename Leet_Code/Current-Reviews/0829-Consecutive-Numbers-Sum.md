# 829. Consecutive Numbers Sum

Given a positive integer N, how many ways can we write it as a sum of
consecutive positive integers?

---

Let's try first 10 sequences and generalize into a pattern:

```
1 = 1
2 = 2
3 = 1 + 2, 3
4 = 4
5 = 2 + 3, 5
6 = 6
7 = 3 + 4, 7
8 = 8
9 = 2 + 3 + 4, 4 + 5, 9
...
N = (x + 1) + (x + 2) + ... + (x + k)
```

We can see that from the last expression, the problem is about incrementing
k and finding the right number for k that which evenly creates N. To solve for
this, our unknown variable here is x; so we isolate for x.

```
Using Gauss summation of 1..k:

N = (k * x) + (k * (k + 1)) / 2

k * x = N - (k * (k + 1)) / 2
```

Here is enough to determine that if the right hand side evaluates to value that
is even multiple of k, then we have a valid consecutive integers. We repeat the
process until we have exhausted all of right hand side.

O(sqrt(n)) in time complexity to due rapidly decreasing right hand side.

---

Python:

```python

class Solution829:

    def consecutiveNumbersSum(self, N):

        result, k = 0, 1
        rhs = N - ((k + 1) * k) // 2

        while rhs >= 0:
            result += rhs % k == 0
            rhs = N - ((k + 2) * (k + 1)) // 2

            
