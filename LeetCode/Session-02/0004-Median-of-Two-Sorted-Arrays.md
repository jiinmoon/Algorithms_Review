# 4. Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return
the median of the two sorted arrays.

---

First naive solution would be to simply merge the two given array into a single
sorted array and find the median. This would take linear time to merge the two
and find the median in constant time. As we are required to merge the two array
into a single one, we would have to dedicate O(m + n) space complexity as well.

To improve upon this, we can take a closer look into the meaning of the median.
The median value not only is the "middle" value, but also a value that evenly
divides the array into two equally sized halfs to its left and right.

Hence, the problem can be thought of as a finding partition point in two array
where their values will balance the number of elements to its left and right.
Also, we should also consider whether these partition point chosen also is in
sorted order by comparing chosen values against each other.

Suppose that we have found a partition point in nums1. Then, we can
automatically find the partition point in nums2 as well as chosen partition
points should equally balance the number of elements to its left and right.

Then, we can compare chosen partition points rank to determine whether they are
"true" median points.

In short, this becomes a binary search problem where the time complexity would
be O(min(m, n)).

---

Python: Simple merge approach.

```python

class Solution4:

    def medianOfTwo(self, nums1, nums2):
        
        nums1 += nums2
        nums1.sort()

        m = len(nums1)

        if m % 2:
            return nums1[m // 2]
        return (nums1[m // 2] + nums1[m // 2 - 1]) * 0.5
```

Python: BinarySerach approach.

```python

class Solution4:

    def medianOfTwo(self, nums1, nums2):
        
        m, n = len(nums1), len(nums2)
        
        # perform binSearch on smaller array
        if m > n:
            return self.medianOfTwo(nums2, nums1)
        
        # edge case where one array is empty
        if not m:
            if n % 2:
                return nums2[n // 2]
            return (nums2[n // 2] + nums2[n // 2 - 1]) * 0.5

        l, r = 0, m - 1

        while l < r:
            # part1 is partition point on nums1
            # part2 is partition point on nums2
            part1 = l + (r - l) * 0.5
            part2 = (m + n + 1) * 0.5 - part1

            # 4 candidates about the partition points
            lmax1 = float('-inf') if part1 == 0 else nums1[part1 - 1]
            lmax2 = float('-inf') if part2 == 0 else nums2[part2 - 1]
            rmin1 = float('inf') if part1 == m else nums1[part1]
            rmin2 = float('inf') if part2 == n else nums2[part2]

            # check whether chosen candidate medians are in correct order
            if lmax1 <= rmin2 and lmax2 <= rmin1:
                lmax = max(lmax1, lmax2)
                rmin = min(rmin1, rmin2)
                if (m + n) % 2 == 0:
                    return (lmax + rmin) * 0.5
                return lmax
            elif lmax1 > rmin2:
                r = part1 - 1
            else:
                l = part1 + 1
```

