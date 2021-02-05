236 Lowest Common Ancestor of a Binary Tree
===========================================

Given a binary tree, find the lowest common ancestor of two given nodes in the
tree.

---

We recursively traverse down the given tree. The base case is when we reach the
leaf or we arrived at either of the given two nodes, in which case we will
return the current node. This is repeated on left and right subtree.

If the subtree on left and right returns the node, then we know that in current
node must be the first node where the two nodes meet on the path up to the root
- hence we will return the current node.

If only one of them returns the node, then current node is not the lowest
common ancestor, but part of the path and the LCA must present above itself; we
will return either node that has been returned from left or right.

Time complexity should be O(n).

---

Python:

```python
class Solution:
    def LCA(self, root, p, q):
        if root in {None, p, q}:
            return root

        left = self.LCA(root.left, p, q)
        right = self.LCA(root.right, p, q)
        
        # p and q are from other sides of tree
        if left and right:
            return root
        
        # p and q are on the same path; return whichever found first
        return left or right
```
