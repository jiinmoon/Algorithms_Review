1060 Missing Element in Sorted Array
====================================

Given a sorted array A of unique numbers, find the K-th missing number starting
from the leftmost number of the array.

---

Consider following:

    [ 1, 2, 6, 7 ] K = 2

We have elements missing from left to right 3, 4, and 5.

This distance of missing can be measured by iterating on the given array and
computing the difference between current and previous. So for example:

    curr = 2, prev = 1  ==> missingCount = 2 - 1 - 1 = 0
    There is no gap between 1 and 2; so no element is missed

    curr = 6, prev = 2 ==> missing count = 6 - 2 - 1 = 3
    This shows that there is two elements missing between 2 and 5

So, we can check whether the k-th to return lies within this segment by
subtracting missing element:

    K = 2 ==> K - missingCount = 2 - 3 = -1

Since no more k-th place to advance, the segment has to lie here, we can return
the value from previous (start of the segment) + the K.

Otherwise, we update the K and prev to advance forward on search.

Time complexity should be of O(n).

---

Python:

```python
class Solution:
    def missingElement(self, nums, K):
        # end of array flag; if encountered, 
        # should just return which ever last element + K-th advanced.
        nums.append(float('inf'))
        
        for i in range(1, len(nums)+1):
            prev, curr = nums[i-1], nums[i]
            missingCount = curr - prev - 1
            if K - missingCount <= 0: return prev + K
            K -= missingCount

        return -1
```

