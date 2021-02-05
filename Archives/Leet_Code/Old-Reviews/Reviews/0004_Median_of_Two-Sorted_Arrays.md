4 Median of Two Sorted Arrays
=============================

Question:
---------

There are two soted arrays **nums1** and **nums2** of size m and
n respectively.

Find the median of two sorted arrays; the time complexity should be O(log
(m+n)).

Solutions:
----------

The time comlexity hints at how the optimal algorithm is going to be like, but
first we would like to explore a naive approach. This can be solved by simply
merging the two arrays into a one sorted array and then find the median
according to the even or odd number of the elements. This is O(m+n).

But the fact that arrays are sorted allows us to find the median candidates
based on its definition. The median by its definition should divide the
elements evenly to its left and right. Thus, we want to find the partition
point in two arrays where once selected, they will divide the it evenly. But
this division has to take into consideration of other array as well since it is
going to be merging. For eexample, if we have

    [1, 10, 20]
    [4, 15, 50]

Then, we could select partition point to be 10, in which case

    [1, 10 | 20]
    [4 | 15, 50]

The above is balanced: 3 to left and 3 to right. Also, the partition point in
first array, 10 is less than the 15 and 4 is less than 20. This in fact, makes
it the candidate for our median.

Choosing the partition point itself can be a binary search algorithm; after we
discovered that partition point chosen is not suitable, then we have selected
a value that is either too great or too low - allowing us to adjust the pointer
accordingly.

Alternatively, we may also use a modified quick sort - quick select algorithm
that find the k-th smallest element where k is the median. We first find the
value of (len(nums1) + len(nums2) + 1) // 2. If the length of the combined
lists are even, then we additionally search for (len(nums1) + len(nums2)) // 2.
And then take the average.

Codes:
------

Python: Binary Search approach.

```python
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        # for convinience, let m be lower.
        if m > n:
            return self.findMedianSortedArray(num2, nums1)
        if not m:
            if (n % 2) == 0:
                return (nums2[n // 2] + nums2[n // 2 - 1]) // 2
            else:
                return nums2[n // 2]
        # binary search for partition point
        lo, hi = 0, m
        while lo <= hi:
            part1 = lo + (hi - lo) // 2
            part2 = (m + n + 1) // 2 - part1
           
            # 4 candidates to consider
            leftMax1 = float('-inf') if part1 == 0 else nums1[part1 - 1]
            leftMax2 = float('-inf') if part2 == 0 else nums2[part2 - 1]
            rightMin1 = float('inf') if part1 == m else nums1[part1]
            rightMin2 = float('inf') if part2 == n else nums2[part2]

            # are the selections correct?
            if (leftMax1 <= rightMin2) and (leftMax2 <= rightMin1):
                leftMax = max(leftMax1, leftMax2)
                if (m + n) % 2 == 0:
                    rightMin = min(rightMin1, rightMin2)
                    return (leftMax + rightMin) / 2
                else:
                    reutrn leftMax
            # wrong candidate, choose new partition points
            elif leftMax1 > rightMin2:
                hi = part1 - 1
            else:
                lo = part + 1
        # error if reached here
        return None
```

---

**Source:**

LeetCode: [Median-of-Two-Sorted-Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays)
