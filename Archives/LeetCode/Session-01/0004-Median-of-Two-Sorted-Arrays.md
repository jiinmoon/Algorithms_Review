# 4. Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return
the median of the two sorted arrays.

Follow up: The overall run time complexity should be O(log (m+n)).

---

First naive approach would be to concatenate the two given arrays into a single
sorted array in O(m + n) time complexity - then, find the median.

We can make improvement by realizing that median is the middle value where it
balances the number of elements to its left and right. Hence, if we can find
a potential division point in one of the array, then we can find another point
in another array where it balances the number of elements to left and right.
If we can find such two points, then we can test for whether elements about the
points are indeed in sorted order to determine whether they are median.

To find such points, we can use binary search algorithm - discard the half of
the array that does not fit. Hence, overall time complexity reduces to O(log (m + n)).

---

Python: Naive concatenation approach.

```python

class Solution4:

    def findMedianOfTwo(self, nums1, nums2):

        nums1 += nums2
        nums1.sort()

        if len(nums1) % 2:
            return nums1[len(nums1) // 2]

        return (nums1[len(nums1) // 2 - 1] + nums1[len(nums1) // 2]) * 0.5
```

Python: Binary Search method.

```python

class Solution4:

    def findMedianOfTwo(self, nums1, nums2):

        m, n = len(nums1), len(nums2)

        if m > n:
            return self.findMedianOfTwo(nums2, nums1)

        if not n:
            if m % 2:
                return nums1[m//2]
            return (nums1[m//2] + nums1[m//2 - 1]) * 0.5

        lo, hi = 0, m

        while lo <= hi:
            
            # choose partition points that balances # of elements in left and right
            part1 = lo + (hi - lo) // 2
            part2 = (m + n + 1) // 2 - partX
            
            # 4 candidates about partition points from two arrays
            leftMax1 = float('-inf') if part1 == 0 else nums1[part1 - 1]
            leftMax2 = float('-inf') if part2 == 0 else nums2[part2 - 1]
            rightMin1 = float('inf') if part1 == m else nums1[part1]
            rightMin2 = float('inf') if part2 == n else nums2[part2]
            
            # choosen candidates are in correct order
            if (leftMax1 <= rightMin2) and (leftMax2 <= rightMin1):
                # even or odd case
                if (m + n) % 2:
                    return max(leftMax1, leftMax2)
                return (max(leftMax1, leftMax2) + min(rightMin1, rightMin2)) * 0.5

            elif leftMax1 > rightMin2:
                hi = part1 - 1
            else:
                lo = part1 + 1
```
