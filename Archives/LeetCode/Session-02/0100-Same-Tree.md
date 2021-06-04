# 100. Same Tree

Given the roots of two binary trees p and q, write a function to check if they
are the same or not.

Two binary trees are considered the same if they are structurally identical,
and the nodes have the same value.

---

We can approach the problem either iteratively or recursively - but the idea is
simple where we would simply move in synchornized fashion on two trees while
comparing current nodes from both binary trees p and q.

---

Python:

```python

class Solution100:

    def isSameTreeRecur(self, p, q):
        
        # if either of them in null, both should be null
        if not (p and q):
            return p == q

        if p.val != q.val:
            return False

        return self.isSameTreeRecur(p.left, q.left) and \
                self.isSameTreeRecur(p.right, q.right)


    def isSameTreeIter(self, p, q):

        queue = [(p, q)]

        def isSame(p, q):
            return p == q if not (p and q) else p.val == q.val

        while queue:

            if not isSame(p, q):
                return False

            if p:
                queue.append((p.left, q.left))
                queue.append((p.right, q.right))

        return True

```
