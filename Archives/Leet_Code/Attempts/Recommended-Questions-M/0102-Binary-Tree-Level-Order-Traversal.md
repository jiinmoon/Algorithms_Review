# 102. Binary Tree Level Order Traversal

Given a binary tree, return the level order traversal of its nodes' values.
(ie, from left to right, level by level).

---

The level order of the binary tree can be acheived with BFS algorithm where by
its nature explores all possible nodes in depth before explore on the next
depth. Thus, at each depth we append the result of the previous depth to our
result.

---

Python:

```python

class Solution:
    def levelOrderTraversal(self, root):
        if not root:
            return []
        q = [root]
        result = []
        while q:
            result.append([node.val for node in q])
            temp = list()
            for node in q:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            q = temp
        return result
```
