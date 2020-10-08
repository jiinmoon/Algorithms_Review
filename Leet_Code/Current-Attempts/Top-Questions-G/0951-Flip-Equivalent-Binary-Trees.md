# 951 Flip Equivalent Binary Trees

For a binary tree T, we can define a flip operation as follows: choose any
node, and swap the left and right child subtrees.

A binary tree X is flip equivalent to a binary tree Y if and only if we can
make X equal to Y after some number of flip operations.

Given the roots of two binary trees root1 and root2, return true if the two
trees are flip equivelent or false otherwise.

---

To determine whether a tree is "flip equivalent", we simply traverse on the
binary tree top to bottom - but as we are doing so, we perform flip traversal
as well as normal traversal. Flip operation simply means that we recursively
traverse downwards with left and right subtree exchanged.

The time complexity remains same as the original as we are not reiterating or
creating more works per recursive calls - the number of calls remains constant.

---

Python:

```python


class Solution:
    def isFlipEquiv(self, p, q):
        if not (p or q):
            return p == q
        if p.val != q.val:
            return False
        # one of two cases must be true as we traverse downwards.
        # 1. normal traversal (moving to left on one tree? we move left on
        # another and vice versa).
        # 2. flip traversal (moving on left on one tree? move to other
        # direction and vice versa).
        return self.isFlipEquiv(p.left, q.left) and self.isFlipEquiv(p.right, q.right) or \
            self.isFlipEquiv(p.left, q.right) and self.isFlipEquiv(p.right, q.left)
```
