# 102. Binary Tree Level Order Traversal

Given the root of a binary tree, return the level order traversal of its nodes'
values. (i.e., from left to right, level by level).

---

To perform level order traversal, we use BFS tree traversal algorithm; as using
FIFO nature of the queue, we can visit the each node's depth level by level.
Hence, at each depth, we store the node's stored in the queue to our result.

---

Python:

```python

class Solution102:

    def levelOrderTraversal(self, root):

        if not root:
            return []

        result = []
        queue = [root]

        while queue:

            result.append( [node.val for node in queue] )
            temp = []

            for node in queue:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)

            queue = temp
        
        return result
```
