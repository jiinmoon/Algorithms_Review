# Min Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root
node down to the nearest leaf node.

---

The tricky part is the path with a single path; in which case, we should simply
return the maximum upwards. But when we have a node with two valid subtrees,
then we should start returning the minimum of the heights encountered.

O(n) in time complexity.

---

Python:

```python

class Solution:

    def minDepth(self, root):
        # base cases: either null or leaf node
        if not root:
            return 0
        if not (root.left or root.right):
            return 1

        l, r = self.minDepth(root.left), self.minDepth(root.right)

        # single path?
        if not (l and r):
            return max(l, r) + 1
        # both subtrees present
        return min(l, r) + 1

```
