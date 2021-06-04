# 101. Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself (i.e.,
symmetric around its center).

---

To check for the symmetry, we can use tree traversal algorithm (either DFS or
BFS) - but group pair of nodes as we visit to the next depths. When we traverse
to left on one node, other should move to the right - and vice versa.

---

Python:

```python

class Solution101:

    def isSymmetricRecur(self, root):

        if not root:
            return True

        def helper(p, q):
            if not (p and q):
                return p == q
            if p.val != q.val:
                return False
            return helper(p.left, q.right) and helper(p.right, q.left)

        return helper(root.left, root.right)


    def isSymmetricIter(self, root):

        if not root:
            return True

        queue = [(root.left, root.right)]

        def isSame(p, q):
            return p.val == q.val if p and q else p == q

        while queue:
            temp = list()

            for p, q in queue:
                if not isSame(p, q):
                    return False
                if p:
                    temp.append( (p.left, q.right) )
                    temp.append( (p.right, q.left) )

        return True
```
