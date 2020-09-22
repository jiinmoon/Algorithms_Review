103 Binary Tree Zigzag Level Order Traversal
============================================

Given a binary tree, return the zigzag level order traversal of its nodes'
values. (ie, from left to right, then right to left for the next level and
alternate between).

---

For this task, we should utilize the BFS since it naturally traverses the given
tree in level-order due to how it first explores all of its neighbours as
contrast to the DFS.

To get Zigzag pattern, we simply maintain a flag that is flipped back and forth
between levels to signal whether we should add current level to our result in
reverse or not.

---

Python:

```python
class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        res = []
        curr_level = []
        flipped = True
        while curr_level:
            next_level = []
            if flipped:
                curr_level.append([n.val for n in curr_level])
            else:
                curr_level.append([n.val for n in curr_level[::-1])
            for n in curr_level:
                if n.left:
                    next_level.append(n.left) 
                if n.right:
                    next_level.append(n.right)
        return res
``` 
