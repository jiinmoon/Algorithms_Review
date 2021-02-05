# Subarray with B Odd Numbers

    Given an array of integers A and an integer B.

    Find the total number of subarrays having exactly B odd numbers.

---

## Approach:

We could naively consider every subarray from size at least B and up, but that
would be O(n^3) in time complexity.

Another approach we can think of is represent odd values in the given list of
integers as 1 and even as 0. Then, the problem becomes finding subarray sum to
B. To do so, we use hashmap to record the prefix sum. Thus, as we iterate
forward, if current (prefix sum - B) exist already in the B, then we have
a valid subarray that has B number of odd elements or B sum of odd elements
represented as 1s.

O(n) in both time and space complexity.

---

Python:

```python

from collections import defaultdict

class Solution:

    def solve(self, A, B):
        
        # odd = 1; even = 0
        A = [ num % 2 for num in A ]

        d = defaultdict(int)
        d[0] = 1

        prefixSum, total = 0, 0

        for num in A:

            prefixSum += num

            if (prefixSum - B) in d:
                total += d[prefixSum - B]

            d[prefixSum] += 1

        return total
```
