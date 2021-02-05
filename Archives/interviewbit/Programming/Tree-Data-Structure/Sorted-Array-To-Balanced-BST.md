# Sorted Array To Balanced BST

    Given an array where elements are sorted in ascending order, convert it to
    a height balanced BST.

    Balanced tree : a height-balanced binary tree is defined as a binary tree in
    which the depth of the two subtrees of every node never differ by more than 1. 

---

We know that inorder traversal on the BST gives us the sorted array. Then, to
create the height-balanced tree, we should have equal amount of nodes to left
and right for every root value chosen; hence, at each depth, we choose mid
value as our root value. Then, we populate the left and right subtree by all
values to the left and right of the chosen root value.

O(n) in time and space complexity due to recursion stack.

---

Python:

```python

class Solution:

    def buildTree(self, arr):

        def helper(l, r):
            if l > r:
                return None

            if l == r:
                return TreeNode(arr[l])

            m = l + (r - l) // 2
            
            node = TreeNode(arr[m])
            node.left = helper(l, m - 1)
            node.right = helper(m + 1, r)

            return node

        return helper(0, len(arr) - 1)
```
