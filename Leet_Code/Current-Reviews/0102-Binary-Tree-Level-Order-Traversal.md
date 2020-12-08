# 102. Binary Tree Level Order Traversal

Given a binary tree, return the level order traversal of its nodes' values.
(ie, from left to right, level by level).

---

Level order traveral on the binary tree can be achieved with BFS algorithm; due
to its nature of discovering all of its neighbours before moving on, BFS will
traverse depth by depth. This would be both O(n) in time and space complexity.

---

Python:

```python

class Solution102:

    def levelOrder(self, root):

        if not root:
            return []

        queue, result = [root], []

        while queue:

            temp = []
            result.append([node.val for node in queue])

            for node in queue:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            queue = temp

        return result
```
