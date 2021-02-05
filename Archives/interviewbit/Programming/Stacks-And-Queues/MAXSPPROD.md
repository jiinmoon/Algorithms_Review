# MAXSPPROD

    You are given an array A containing N integers. The special product of each
    ith integer in this array is defined as the product of the following:

    LeftSpecialValue: For an index i, it is defined as the index j such that
    A[j]>A[i] and (i>j). If multiple A[j]'s are present in multiple positions,
    the LeftSpecialValue is the maximum value of j.

    RightSpecialValue: For an index i, it is defined as the index j such that
    A[j]>A[i] and (j>i). If multiple A[j]'s are present in multiple positions,
    the RightSpecialValue is the minimum value of j.

    Write a program to find the maximum special product of any integer in the array.


    NOTE: As the answer can be large, output your answer modulo 109 + 7.


---

## Approach:

We need to know for each index, whether we can find the left and right special
values. For this, we use stack and interate from front and back to record the
special values found.

O(n) in both time and space complexity.

---

Python:

```python

class Solution:

    def maxSpeicalProduct(self, A):
        
        lsv = [0] * len(A)
        rsv = [0] * len(A)
        stack = [0]
        
        for i in range(1, len(A)):
            while stack and A[stack[-1]] < A[i]:
                rsv[stack.pop()] = i
            stack.append(i)
        
        stack = []
        
        for i in range(len(A)-1, -1, -1):
            while stack and A[stack[-1]] < A[i]:
                lsv[stack.pop()] = i
            stack.append(i)
        
        result = 0
        for l, r in zip(lsv, rsv):
            result = max(result, l * r)
        
        return result % (10**9 + 7)
```
