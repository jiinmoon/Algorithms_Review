# 236. LCA of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes
in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is
defined between two nodes p and q as the lowest node in T that has both p and
q as descendants (where we allow a node to be a descendant of itself).”

---

To identify the LCA of the binary tree, we recursivly traverse down on the
given tree. If we encounter a node that matches either given nodes, then we can
start to return the current node that has that node as its child. When we find
the both left and right subtree returns the node, then current node is the LCA;
otherwise, we propagate up whichever node that has been found thus far.

---

Python:

```python

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root in {None, p, q}:
            return root

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        # p and q are found; return current which is the LCA
        if l and r:
            return root
        return l or r
```
