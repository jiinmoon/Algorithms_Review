42 Trapping Rain Water
======================

Given _n_ non-negative integers representing an elevation map where the width
of each bar is 1, compute how much water it is able to trap after raining.

---

We can think of the problem as a collection of cells where water is trapped on
its side. Each cell can contain water as high as minimum of heights to its left
and right.

Then, we can iterate on each cell, and find the minimum of left and right
heights to compute the amount of water that it can hold; and return the total.

The problem is the computing the left and right heights at each cell - there
are too many duplicate works being done here. To reduce this, we should be
storing the max heights values from left and right. This can result in O(n)
time complexity but also requires O(n) space as well.

But as we compute above way, we notice that when we hit the height that is
greater than another, as long as its height remains great, all we need to do is
move the other pointer - and swap if heights become smaller. Using two
pointers, we can avoid having to store all the max height values and reference
them.

---

Go:

Switching two pointers method.

```go
func trap(height []int) int {
    var (
        l = 0
        r = len(height)-1
        ans = 0
        lMax = 0
        rMax = 0
    )
    for l < r {
        // move the min height
        if height[l] < height[r] {
            // update lMax if curr height is greater
            if height[l] > lMax {
                // if current height is greater than lMax, it implies that the
                // cell does not contain water.
                lMax = height[l]
            } else {
                // current cell is lower than lMax; update ans
                ans += (lMax - height[l])
            }
            l++
        } else {
            if heights[r] > rMax {
                rMax = height[r]
            } else {
                ans += (rMax - height[r])
            }
            r--
        }
    }
    return ans
}
```

