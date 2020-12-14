# 100. Same Tree

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and
the nodes have the same value.

---

A simple method would be to traverse on each of the nodes, then compare them.
At each node their values must match. Time and space complexity would be O(n).

---

Python: recursive dfs.

```python

class Solution100:

    def isSameTree(self, p, q):

        if not (p and q):
            return p == q

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```

Python: iterative traversal.

```python

class Solution100:

    def isSameTree(self, p, q):

        queue = [(p, q)]

        def areSameNodes(p, q):
            return p.val == q.val if p and q else p == q

        while queue:

            temp = list()

            for p, q in queue:

                if not areSameNodes(p, q):
                    return False

                if p:
                    temp.append((p.left, q.left))
                    temp.append((p.right, q.right))
            
            queue = temp

        return True
```
