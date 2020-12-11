# 101. Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric
around its center).

---

We can check for symmetry by having two entry point into the same tree - at
each depth we visit them in mirror fashion.

O(n) time complexity.

---

Python: recursive.

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

Python: iterative BFS.

```python

class Solution101:

    def iSymmetric(self, root):

        if not root:
            return True

        queue = deque([root.left, root.right])

        def isSame(p, q):
            if not (p and q):
                return p == q
            return p.val == q.val


        while queue:
            
            p, q = queue.popleft()

            if not isSame(p, q):
                return False

            if p:
                queue.append((p.left, q.right))
                queue.append((p.right, q.left))

        return True
```
