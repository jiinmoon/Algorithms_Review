# 863 All Nodes Distance K in Binary Tree

We are given a binary tree (with root node root), a target node, and an integer
value K.

Return a list of the values of all nodes that have a distance K from the target
node.  The answer can be returned in any order.

---

First, we can traverse on the binary tree in search of the target node. From
here, we can recursively traverse downard to find the nodes that may present
starting from target node to downward. Here, the problem is not finding the
node that is on the other side of the target node - to resolve this, we have
each node once found the target node, return an identifier that it has found
the target node. Depending on its value, we can determine whether we can search
the other side of the tree from the parent of the target node.

---

Python:

```python

class Solution:
    def findAllNodesDistK(self, root, target, k):
        def searchDownward(node, d):
            if not node:
                return
            if d == 0:
                res.append(node)
                return
            searchDownward(node.left, d - 1)
            searchDownward(node.right, d - 1)

        def searchAll(node):
            if not node:
                return -1
            if node == target:
                searchDownward(node, k)
                return 0
            l, r = searchAll(node.left), searchAll(node.right)
            d = 1 + max(l, r)
            if k - d == 0:
                searchDownward(node, 0)
            elif k - d > 0:
                otherside = node.left if l == -1 else node.right
                searchDownward(otherside, d - k - 1)
            return d
        
        res = list()
        searchAll(root)
        return res
```
