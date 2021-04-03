# 108. Convert Sorted Array to Binary Search Tree

Given an integer array nums where the elements are sorted in ascending order,
convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two
subtrees of every node never differs by more than one.

---

To create a height-balanced BST, for each node, we should divide the elements
to equal number to its left and right where left subtree is populated by
elements less than current node, and vice versa. Hence, we repeatedly select
the mid element to be our current node for recursive call, and at each depth,
we divide the array into equal halves to repeat on next recursive depth.

---

Python:

```python

class Solution108:

    def sortedArrayToBST(self, nums):
        
        def helper(l, r):
            if l > r:
                return None

            m = l + (r - l) // 2
            currNode = TreeNode(nums[m])
            currNode.left = helper(l, m - 1)
            currNode.right = helper(m + 1, r)

            return currNode

        return helper(0, len(nums) - 1)
```
