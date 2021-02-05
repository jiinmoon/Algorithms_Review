# Symmetric Binary Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric
around its center).

---

Recursively check on its left and right swapped.

O(n) in time complexity.

---

Python:

```python

class Solution:

    def isSymmetric(self, root):

        def _check(p, q):

            if not (p and q):
                return p == q

            if p.val != q.val:
                return False

            return _check(p.left, q.right) and _check(p.right, q.left)

        return 1 if _check(root.left, root.right) else 0

```
