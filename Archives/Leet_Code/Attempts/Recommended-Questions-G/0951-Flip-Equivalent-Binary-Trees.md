# 951. Flip Equivalent Binary Trees

For a binary tree T, we can define a flip operation as follows: choose any
node, and swap the left and right child subtrees.

A binary tree X is flip equivalent to a binary tree Y if and only if we can
make X equal to Y after some number of flip operations.

Given the roots of two binary trees root1 and root2, return true if the two
trees are flip equivelent or false otherwise.

---

To find whether given two binary trees are flip equivalent, we recursive
traverse and check to see whether the two given trees are identical while
flipping the nodes.

---

Python:

```python

class Solution:
    def isFlipEquiv(self, p, q):
        if not (p or q):
            return p == q
        if p.val != q.val:
            return False
        # either is same for normal traversal or is same for flip traversal
        return (self.isFlipEquiv(p.left, q.left) and self.isFlipEquiv(p.right, q.right) \
            || (self.isFlipEquiv(p.left, q.right) and self.isFlipEquiv(p.right, q.left)
```
