107 Binary Tree Level Order Traversal II
========================================

Question:
---------

Given a binary tree, return the _bottom-up level order_ traversal of its nodes'
values.

Solutions:
----------

The problem is easily solved with BFS algorithm using queue since it by its
nature traverses in level-order. Or, we could use an inorder traversal as well.
Either case, it will be in O(n) time complexity.

Codes:
------

Python: BFS

```python
class Solution:
    def levelOrderBottom(self, root):
        results = []
        queue = [root]
        while queue:
            m = len(queue)
            results.append(queue.copy())
            for _ in range(m):
                curr = queue.pop(0)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return results[::-1]
```

---

**Source:**

LeetCode: [Binary-Tree-Level-Order-Traversal-II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/))
