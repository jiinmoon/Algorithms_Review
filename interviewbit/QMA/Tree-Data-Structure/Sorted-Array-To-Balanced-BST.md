# Sorted Array To Balanced BST

Given an array where elements are sorted in ascending order, convert it to
a height balanced BST.

 Balanced tree : a height-balanced binary tree is defined as a binary tree in
 which the depth of the two subtrees of every node never differ by more than 1. 

---

We can build the height-balanced BST by repeatedly taking the mid element as
a root and populate left and right subtree as lower and upper half of the array
pivoted by the middle element. O(n) in time complexity.

---

Python:

```python

class Solution:

    def sortedArrayToBST(self, arr):

        def _build(l, r):
            if l > r:
                return

            m = l + (r - l) // 2

            node = TreeNode(arr[m])
            node.left = _build(l, m - 1)
            node.right = _build(m + 1, r)

            return node

        return _build(0, len(arr) - 1)
```
