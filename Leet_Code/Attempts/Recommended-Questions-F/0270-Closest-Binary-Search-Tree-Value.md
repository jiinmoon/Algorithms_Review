# 270. Closest Binary Search Tree Value

Given a non-empty binary search tree and a target value, find the value in the
BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to
the target.

---

This is essentially a binary search algorithm - finding the insertion point for
target value. Starting from the root, we compare the current node's value to
our closest value that we have found thus far. If it is same, then we can
return it right away. Otherwise, we compare the absolute difference between the
value that we have found thus far and the diff of current node's value to
target value. Then, we move down the tree left or right based on the target
value. The time complexity should be of O(log(n)).

---

Python:

```python

class Solution:
    def closestValue(self, root, target):
        closestThusFar = root.val
        while root:
            if root.val == target:
                return root.val

            # update closest value found thus far based on abs difference
            if abs(root.val - target) < abs(closestThusFar - target):
                closestThusFar = root.val

            if target < root.val:
                root = root.left
            else:
                root = root.right

        return closestThusFar
```


