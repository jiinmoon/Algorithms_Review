102 Binary Tree Level Order Traversal
=====================================

Given a binary tree, return the level order traversal of its nodes' values.

---

A simple BFS traversal on the tree will yield the level order; time complexity
should be of O(v + e).

---

Python:

```python

class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        q = [ root ]
        res = list()

        while q:
            res.append([node.val for node in q])
            temp = list()
            for node in q:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            q = temp

        return res
```
