# 104. Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path
from the root node down to the farthest leaf node.

---

We can easily solve this problem using the recursion and definition of the
binary tree. First, we traverse all the way down to the bottom - starting from
leaf nodes, we start to return the maximum depths found below from two child
nodes plus one more including the current node upwards to the parent function
call left in the stack.

---

Python:

```python

class Solution104:

    def maxDepth(self, root):

        if not root:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
```
