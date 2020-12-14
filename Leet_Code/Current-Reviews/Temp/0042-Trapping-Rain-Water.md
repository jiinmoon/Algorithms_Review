# 42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of
each bar is 1, compute how much water it can trap after raining.

---

(1) Brute Force.

We can find the total amount of water trapped in the given heights by sum of
individual waters trapped at each bar. Then, the trapped water at each bar
would be bounded by minimum of two maximum bars to its left and right. Naive
approach would be to at each cell, perform linear search to left and right to
find the maximum bars. This would be O(n^2) in time complexity and O(1) in
space complexity.

(2) Record left and right maximum heights.

Instead of searching every time at element, we prepare two arrays to record the
min and max heights at each position. By doing this, we can reduce the time
complexity to O(n) but space complexity would be O(n).

(3) Two Pointers.

If we use two pointers, then we can compare two heights at these pointers and
move the smaller one. By doing so, we do not have to maintain any extra
information about maximum heights as we are recording them as a single variable
as we iterate and only one of them is changing at a time. Hence, time
complexity would be O(n) and space complexity would be O(1).

---

Java:

```java

class Solution42 {

    public int trap(int[] height)
    {
        int l = 0, r = height.length - 1;
        int lmax = 0, rmax = 0, total = 0;

        while (l < r)
        {
            if (height[l] < height[r]) {
                lmax = Math.max(lmax, height[l]);
                total += lmax - height[l];
                l++;
            } else {
                rmax = Math.max(rmax, height[r]);
                total += rmax - height[r];
                r--;
            }
        }

        return total;
    }
}

```

Python:

```python

class Solution42:

    def trap(self, height):

        l, r = 0, len(height)-1
        lmax, rmax, total = 0, 0, 0

        while l < r:

            if height[l] < height[r]:
                lmax = max(lmax, height[l])
                total += lmax - height[l]
                l += 1
            else:
                rmax = max(rmax, height[r])
                total += rmax - height[r]
                r -= 1

        return total
```


