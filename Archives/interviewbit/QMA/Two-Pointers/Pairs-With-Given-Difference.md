# Pairs With Given Difference

Given an one-dimensional unsorted array A containing N integers.

You are also given an integer B, find if there exists a pair of elements in the
array whose difference is B.

Return 1 if any such pair exists else return 0.

---

### (1) Naive Brute Force.

Iterate to examine all pairs to check whether their difference can make up for
the target B. O(n^2) in time complexity.

### (2) Sort first, then use two pointers from both ends.

By sorting, we have a direction as to how to increment or decrement our current
selection of pairings depending on their differences. O(n * log(n)) to sort.

### (3) Use Set.

Use set data structure to record (num + target) and (num - target). O(n) in
time complexity and space complexity.

---

Python: Set.

```python

class Solution:

    def hasPairs(self, A, B):

        seen = set()

        for num in A:
            
            if num in A:
                return 1

            seen.add(num + B)
            see.add(num - B)

        return 0
```
