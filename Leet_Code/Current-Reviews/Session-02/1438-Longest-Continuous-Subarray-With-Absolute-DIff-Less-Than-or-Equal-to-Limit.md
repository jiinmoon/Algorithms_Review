1438 Subarray with Absolute Diff <= Limit
=========================================

Given an array of integers nums and an integer limit, return the size of the
longest non-empty subarray such that the absolute difference between any two
elements of this subarray is less than or equal to limit.

---

If we try to brute force this, we can try to consider every possible subarray
to check for its maximum diff within the elements between the subarray. O(n**2)
to generate all the arrays and O(n) for each subarray to find min/max - thus,
O(n**3).

While doing so, we notice that we are only interested in the maximum of the
subarray and the minimum of the subarray - and its difference to check against
the given limit.

The idea is as follows: we will first prepare two queues where one will be used
to store the maximum values and other for minimum values as we iterate on the
given array from left to right.

The new leftmost value we are encountered with is either max or min; 

As we iterate, we update both of the queues; from the back, we need to pop out
the values that are smaller (if maxQ) or greater (if minQ). By doing so, we can
maintain the decreasing order of maxes and increasing order of mins to compute
the next differences without having to iterate to find next maxes/mins. Then,
we push in the current value under right pointer to the queues.

This way current subarray between the left and right pointers is computed by
taking the abs diff from the front of the two queues.

If this diff is greater than the limit, then we need to scale inwards - from
either queue, if their front values are equal to the value under the left
pointer, we pop. This will choose the next max and mins to consider in next
subarray. Then increment the left pointer.

The right pointer will advance as always and longest subarray length is always
measured with (right - left + 1).

This can be achieved in O(n).

---

Python:

```python
from collections import deque

class Solution:
    def longestSubarr(self, nums, lim):
        left, right = 0, 0
        longestThusFar = 0
        maxQ, minQ = deque(), deque()

        while right < len(nums):
            curr = nums[right]
            # update the Qs
            while maxQ and maxQ[-1] < curr: maxQ.pop()
            while minQ and minQ[-1] > curr: minQ.pop()
            maxQ.append(curr)
            minQ.append(curr)

            # current abs diff from arr[left:right]
            diff = abs(maxQ[0] - minQ[0])

            # if diff is greater than limit
            # scale inwards by moving left + 1
            # which value was under left pointer?
            if diff > lim:
                if maxQ[0] == nums[left]: maxQ.popleft()
                if minQ[0] == nums[left]: minQ.popleft()
                left += 1

            # update longestThusFar
            longestThusFar = max(longestThusFar, right - left + 1)
            right += 1

        return longestThusFar
```
