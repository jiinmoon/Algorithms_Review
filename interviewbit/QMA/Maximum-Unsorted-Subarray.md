# Maximum Unsorted Subarray

You are given an array (zero indexed) of N non-negative integers, A0, A1 ,…,
AN-1.

Find the minimum sub array Al, Al+1 ,…, Ar so if we sort(in ascending order)
that sub array, then the whole array should get sorted.
If A is already sorted, output -1.

---

This is about finding the min and max of the unsorted regions.

First, starting from the left, we find the first index where unsorted region
begins which is marked by first element that is lesser than the previous
element. From here on, we record the minmum value thus far.

Next, starting from the right, we also find the first index where unsorted
region starts which is marked by first element that is greater than previous;
starting from this point record the max value.

Now, we have min and max values of our unsorted region; next we need to find
their insertion points or their correct indicies in "sorted" region. We iterate
from left and right to find their positions and record.

O(n) in time complexity and O(1) in space complexity.

---

Python:

```python
class Solution:

    def subUnsort(self, A):
        
        minThusFar, maxThusFar = float('inf'), float('-inf')
        
        found = False
        for i in range(1, len(A)):
            if A[i] < A[i-1]:
                found = True
            if found:
                minThusFar = min(minThusFar, A[i])
                
        found = False;
        for i in range(len(A)-2, -1, -1):
            if A[i] > A[i+1]:
                found = True
            if found:
                maxThusFar = max(maxThusFar, A[i])
                
        left = 0
        while left < len(A):
            if minThusFar < A[left]:
                break
            left += 1
        
        right = len(A) - 1
        while right >= 0:
            if maxThusFar > A[right]:
                break
            right -= 1
  	
	if (right - left) < 0:
	    return [-1]
        return [left, right]
```
