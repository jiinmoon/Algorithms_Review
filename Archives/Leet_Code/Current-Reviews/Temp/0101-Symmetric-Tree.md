# 101. Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric
around its center).

---

We traverse on the tree; but we traverse to its left and right subtree
separately. At each nodes they should be same; otherwise, we move down while
moving in mirrored fashion.

Time and space complexity would be O(n).

---

Python: iterative traversal.

```python

class Solution101:

    def isSymmetric(self, root):

        if not root:
            return True

        queue = [(root.left, root.right)]

        def areSameNodes(p, q):
            return p.val == q.val if p and q else p == q


        while queue:

            temp = list()

            for p, q in queue:
                
                if not areSameNodes(p, q):
                    return False

                if p:
                    temp.append((p.left, q.right))
                    temp.append((p.right, q.left))

            queue = temp

        return True
```

Python: recursive traversal.

```python

class Solution101:

    def isSymmetric(self, root):

        if not root:
            return True

        def helper(p, q):
            if not (p and q):
                return p == q

            if p.val != q.val:
                return False

            return helper(p.left, q.right) and helper(p.right, q.left)

        return helper(root.left, root.right)
```
