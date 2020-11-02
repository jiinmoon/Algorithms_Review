# 103. Binary Tree Zigzag Level Order Traversal

Given a binary tree, return the zigzag level order traversal of its nodes'
values. (ie, from left to right, then right to left for the next level and
alternate between).

---

We can retrieve the level order of the binary tree by performing BFS which
explores the given tree depth by depth. Hence, it would be simple matter of
reversing the current list of nodes at each depth.

---

Python:

```python

class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        result = list()
        q = [root]
        flip = False
        while q:
            if flip:
                result.append([node for node in q])
            else:
                result.append([node for node in q[::-1])
            flip = not flip
            temp = list()
            for node in q:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            q = temp

        return result[::-1]
```
