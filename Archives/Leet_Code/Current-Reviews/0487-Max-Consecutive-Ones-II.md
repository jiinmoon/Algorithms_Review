# 487. Max Consecutive Ones

Given a binary array, find the maximum number of consecutive 1s in this array
if you can flip at most one 0.

---

Use two-pointers to maintain the sliding window. We expand out to right while
counting the zeroes encountered. If we find that our count of zeroes have
exceeded the limit (here is 1), we decrement our start of window by moving
left pointer to next. Then, record the maximum of these subarrays found thus
far.

O(n) in time complexity.

---

```python

class Solution487:

    def maxConsecutiveOnes(self, nums):

        l, r, zeroes, maxThusFar = 0, 0, 0, 0

        while r < len(nums):
            
            if zeroes <= 1:
                zeroes += nums[r] == 0
                r += 1

            if zeroes > 1:
                zeroes -= nums[l] == 0
                r += 1

            maxThusFar = max(maxThusFar, r - l)

        return maxThusFar
```
