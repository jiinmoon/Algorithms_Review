# 863 All Nodes Distance K in Binary Tree

We can perform a simple downward traversal search to K depths. The problem is
that there may be another nodes above and other paths from the target node. To
resolve this, we have each node to return an indicator for target. Then, search
the otherside if we can.

---

Python:

```python

class Solution:
    def allNodesDistK(self, root, target, k):
        def searchdown(node, d):
            if not node:
                return
            if d == 0:
                res.append(node.val)
                return
            searchdown(node.left, d-1)
            searchdown(node.right, d-1)

        def searchall(node):
            if not node:
                return -1
            if node == target:
                searchdown(node, k)
                return 0
            l, r = searchall(node.left), searchall(node.right)
            if l == r = -1:
                return -1
            d = 1 + max(l, r)
            if k - d == 0:
                searchdown(node, 0)
            elif k - d > 0:
                otherside = node.left if l == -1 else node.right
                searchdown(otherside, k - d - 1)
            return d

        res = list()
        searchall(root)

        return res
```
