# 4. Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return
the median of the two sorted arrays.

Follow up: The overall run time complexity should be O(log (m+n)).

---

Naive approach on this problem should be merging two sorted list into a single
merged list where we can easily find the median. However, the time complexity
of this approach is O(n + m) due to merging involved, and same for space
complexity as well.

To be able to achieve the time complexity of O(log (m + n)), we use binary
search algorithm. We can view this problem as a finding a partition point in
two lists where it will divide the two arrays into left and right collections
of elements that are "balanced". Once this is achieved we have potential
candidates about the partition points that can be median or "middle" points. If
the maximum value from the left array is less than or equal to the minimum
value from the right array, then iwe have found partition points that cleanly
divides the array into equal halves in sorted fashion.

---

Java:

```java

class Solution {
    public double findMedianSortedArray(int[] nums1, int[] nums2) {
        m = nums1.length;
        n = nums2.length;
        
        // work with smaller array for binary search
        if (m > n)
            return findMedianSortedArray(nums2, nums1);

        // edge case - nums1 is empty
        if (m == 0)
            return (n % 2 != 0) ? nums2[n/2] : (nums2[n/2] + nums2[n/2-1]) * 0.5;

        int lo = 0;
        int hi = m;

        while (lo <= hi) {
            int part1 = lo + (hi - lo) / 2;
            int part2 = (m + n + 1) / 2 - part1;
            
            int leftMax1 = (part1 == 0) ? Integer.MIN_VALUE : nums1[part1 - 1];
            int leftMax2 = (part2 == 0) ? Integer.MIN_VALUE : nums2[part2 - 1];
            int rightMin1 = (part1 == m) ? Integer.MAX_VALUE : nums1[part1];
            int rightMin2 = (part2 == n) ? Integer.MAX_VALUE : nums2[part2];

            if (leftMax1 <= rightMin2 && leftMax2 <= rightMin1) {
                int left = Math.max(leftMax1, leftMax2);
                int right = Math.min(rightMin1, rightMin2);
                return ((m + n) % 2 != 0) ? left : (left + right) * 0.5;
            } else if (leftMax1 > rightMin2) {
                hi = part1 - 1;
            } else {
                lo = part1 + 1;
            }
        }

        return -1.0 // error
    }
}

```

Python:

```python

class Solution:
    def findMedianOfTwo(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        
        # maintain smaller array to left
        if m > n:
            return self.findMedianOfTwo(nums2, nums2)

        # edge case of non-exsiting nums1
        if not m:
            if n % 2:
                return nums2[n//2]                      # odd
           return (nums2[n//2] + nums[n//2-1]) * 0.5    # even

        # binary search for partition points to balance two arrays
        # find point in one will find another as numbers need to balance
        l, r = 0, m - 1
        while l <= r:
            part1 = l + (r - l) // 2
            part2 = (m + n + 1) // 2 - part1

            lMax1 = float('-inf') if part1 == 0 else nums1[part1 - 1]
            lMax2 = float('-inf') if part2 == 0 else nums2[part2 - 1]
            rMin1 = float('inf') if part1 == m else nums1[part1]
            rMin2 = float('inf') if part2 == n else nums2[part2]
            
            if (lMax1 <= rMin2) and (lMax2 <= rMin2):
                if (m + n) % 2:
                    return max(lMax1, lMax2)                            # odd
                return (max(lMax1, lMax2) + min(lMin1, rMin2)) * 0.5    # even
            elif lMax1 > rMin2:
                r = part1 - 1
            else:
                l = part1 + 1
```
