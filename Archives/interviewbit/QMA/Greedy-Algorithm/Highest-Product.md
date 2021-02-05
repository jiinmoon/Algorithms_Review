# Highest Product

Given an array A, of N integers A.

Return the highest product possible by multiplying 3 numbers from the array.

NOTE: Solution will fit in a 32-bit signed integer.

---

First sort the given array. Then, we have two candidates:

(1) All positives mean that we have our maximum product by taking three
largest.

(2) Some negatives mean that we can potentially create max product by taking
two minimums and one maximum value.

O(n * log(n)) due to sorting involved.

---

Python:

```python

class Solution:
    # @param A : list of integers
    # @return an integer
    def maxp3(self, A):
        
        A.sort()
        
        maxNum1, maxNum2, maxNum3 = A[-1], A[-2], A[-3]
        minNum1, minNum2 = A[0], A[1]
        
        return max(maxNum1 * minNum1 * minNum2, maxNum1 * maxNum2 * maxNum3)

```
