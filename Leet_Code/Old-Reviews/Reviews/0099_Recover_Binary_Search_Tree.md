99 Recover Binary Search Tree
=============================

Question:
---------

The value of two nodes are swapped in the binary search tree; find them, and
fix the tree without changing its structure.

Solutions:
----------

We utilize the fact that in-order traversal on the BST gives us an ordered list
of values within the tree. So, we perform a traversal while keeping track of
the previous value, and when we find the out of order element, we save it
pointer and swap with next node that is out of its place. This is a linear
algorithm.

Codes:
------

Python:

```python
class Solution:
    def recoverTree(self, root):
        node1, node2 = None, None
        prev = TreeNode(float('-inf))

        def inorder(node):
            if not node:
                return
            # recurisvely visit down to leftmost node 
            inoder(node.left)
            # starting here, find the out of place nodes.
            # nodes should be increasing order, thus if less than the prev, it
            # to be the swapped node.
            if node.val <= prev.val:
                if not node1:
                    node1 = prev
                if node1:
                    node2 = node
            prev = node
            inorder(node.right)
        
        inorder(root) 
        node1.val, node2.val = node2.val, node1.val
```

---

**Source:**

LeetCode:
[Recover-BST](https://leetcode.com/problems/recover-binary-search-tree/)
