# Distinct Numbers in Window

    You are given an array of N integers, A1, A2 ,..., AN and an integer B. Return
    the of count of distinct numbers in all windows of size B.

    Formally, return an array of size N-B+1 where i'th element in this array
    contains number of distinct elements in sequence Ai, Ai+1 ,..., Ai+B-1.

    NOTE: if B > N, return an empty array.

---

## Approach:

Use hashmap to count the elements encountered. We first iterate upto B to
compute the counts for elements present within the first window. Then, we
iterate to add new elements (i - k) and remove previous starting element at
(i). Whenever removed element reaches 0, we decrease the count of distinct
elements and vice versa.

O(n) in time complexity.

---

```python

from collections import defaultdict

class Solution:

    def distinctNumbers(self, A, B):

        count, d = 0, defaultdict(int)
        for num in A[:B]:
            count += num not in d
            d[num] += 1

        result = [count]
        for i in range(B, len(A)):
            count -= d[A[i - B]] == 1
            d[A[i - B]] -= 1

            count += d[A[i]] == 0
            d[A[i]] += 1

            result.append(count)
        
        return result
```
