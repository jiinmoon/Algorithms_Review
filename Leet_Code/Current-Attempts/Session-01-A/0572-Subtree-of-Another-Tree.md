# 572 Subtree of Another Tree

Two general approachs are valid here. One is to serialize the tree or record
the chosen traversal order of the tree to pattern match against another. Other
approach would be to perform a recrusive traversal on the given tree - and
search down on each node.

---

Python:

```python

class Solution:
    def isSameTree(self, p, q):
        if not (p and q):
            return p == q
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSubtree(self, S, T):
        if not S:
            return False
        return self.isSameTree(S, T) or self.isSubtree(S.left, T) or self.isSubtree(S.right, T)
```


