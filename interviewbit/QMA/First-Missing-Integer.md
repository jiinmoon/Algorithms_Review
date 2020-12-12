# First Missing Integer

Given an unsorted integer array, find the first missing positive integer.

---

If this positive integer exists, it must lie within the range of the [0 .. n]
where n is the length of the given array. Hence, for every positive number
encountered, we mark the positions where they are found with its index.

Then, we iterate forward to find first non-marked index. If all are marked,
then all positive numbers are present and next missing integer is n + 1.

O(n) in time complexity and O(1) in space complexity.

---

Python:

```python

class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):

        A.append(0)
        
        for num in A:
            while num != "#" and 0 < num < len(A):
                A[num], num = "#", A[num]
        
        for i, num in enumerate(A[1:], 1):
            if num != "#":
                return i

        return len(A)

```
