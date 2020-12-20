# Symmetric Binary Tree

    Given a binary tree, check whether it is a mirror of itself (ie, symmetric
    around its center).

---

## Approach:

We can check for whether given tree is a mirror image or not by having a two
entry point into the same tree and traverse in mirror fashion.

O(n) in time complexity.


---

Python:

```python

class Solution:

    def isSymmetric(self, root):

        def helper(p, q):
            
            if not (p and q):
                return p == q

            if p.val != q.val:
                return False

            return helper(p.left, q.right) and helper(p.right, q.left)

        return helper(root.left, root.right)

```
