# LeetCode Daily Challenge: August Week.2 - Day.1

## Question

Given a non-empty binary search tree and a target value, find the value in the
BST that is closest to the target.

Note:

- Given target value is a floating point.

- You are guaranteed to have only one unique value in the BST that is closest to
the target.

## Solution

We iterate on the given tree based on the current node's value - if it is less
than target, then the closest value lie in leftsubtree and vice versa. While we
are utilizing the fact that this is a BST, and average runtime would be in
O(n), because of the case where we may have a linked list as a given tree, the
big-O is bounded at O(n).

Go:

```
import "math"

func closestValue(root *TreeNode, target float64) int {
    closest = root.Val
    for root != nil {
        rVal64 := float64(root.Val) 
        if rVal64 == target {
            return rVal64
        }

        diff1 := math.Abs(rVal64 - target)
        diff2 := math.Abs(float64(closest) - target)
        if diff1 < diff2 {
            closest = root.Val
        }

        if target < rVal64 {
            root = root.Left
        } else {
            root = root.Right
        }
    }
    return closest
}
```

Python:

```python
class Solution:
    def closestValue(self, root, target):
        closestThusFar = root.val
        while root:
            if root.val == target:
                return target
            if abs(root.val - target) < abs(closestThusFar - target):
                closestThusFar = root.val
            if root.val > target:
                root = root.left
            else:
                root = root.right
        return closestThusFar
```

