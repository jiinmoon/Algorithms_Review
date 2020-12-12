# Repeat and Missing Number Array

You are given a read only array of n integers from 1 to n.

Each integer appears exactly once except A which appears twice and B which is
missing.

Return A and B.

Note: Your algorithm should have a linear runtime complexity. Could you
implement it without using extra memory?

Note that in your output A should precede B.

---


### (1) Iterate to find duplicate element.

Use O(n) space to count each element to find the duplicate element. Then,
missing element should be sum(expected) + sum(actual) - duplicate.

### (2) Math.

We can find the missing and expected element by using a bit of math.

```

Let Sa be sum of given array and Se be sum of expected array (all elements from
1 to n are present). Then, following statement is true:

            Sa = Se + (missing) - (duplicate)

Let M to denote missing element and D to denote duplicate element.

    S1:    Sa - Se = M - D

To solve for M and D, we need another True statement; let us examine sum of
squares from each. Let SQa be sum of squared elements of given array and SQe be
sum of sequared elements from expected array.

            SQa - SQe = M^2 - D^2
    S2:     SQa - SQe = (M + D) * (M - D)

Let's divide S2 by S1:

    S3:     (SQa - SQe) / (Sa - Se) = (M + D) * (M - D) / (M - D)
            (SQa - SQe) / (Sa - Se) = M + D

We can now solve for M and D by substitution:

    S1 + S3:

            (Sa - Se) + (SQa - SQe) / (Sa - Se) = M - D + M + D
            (1/(Sa - Se)) * (1 + (SQa - SQe)) = 2M

Thus,

            M = 0.5 * (1/(Sa - Se)) * (1 + (SQa - SQe))
```

This method will not require any space and solve in O(n) time.

---

Python: Count approach.

```python

from collections import Counter

class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        
        counter = Counter(A)
        
        duplicate = max(counter.items(), key=lambda x : x[1])[0]
        
        actualSum = sum(A)
        expectedSum = sum(i for i in range(1, len(A) + 1))
        
        missing = expectedSum - actualSum + duplicate
        
        return [duplicate, missing]

```

Python: Math hammer.

```python

class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        
        n = len(A) + 1
        sum1 = sum(A)
        sum2 = sum(i for i in range(1, n))
        
        sq1 = sum(num**2 for num in A)
        sq2 = sum(i**2 for i in range(1, n))
        
        s1 = sum1 - sum2
        s2 = sq1 - sq2
        
        duplicate = 0.5 * ((s2/s1) + s1)
        missing = a - s1
        
        return [int(duplicate), int(missing)]

```
