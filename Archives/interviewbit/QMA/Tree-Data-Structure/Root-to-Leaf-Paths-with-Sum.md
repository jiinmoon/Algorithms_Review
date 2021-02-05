# Root-to-Leaf-Paths-with-Sum

Given a binary tree and a sum, find all root-to-leaf paths where each path’s
sum equals the given sum.

---

Python:

```python

class Solution:

    def pathSum(self, A, B):

        def traverse(path, pathSum, node):

            if not node:
                return

            pathSum += node.val
            if not (node.left or node.right) and pathSum == B:
                result.append(path + [node.val])
            else:
                traverse(path + [node.val], pathSum, node.left)
                traverse(path + [node.val], pathSum, node.right)

        result = []
        traverse([], 0, A)

        return result
```
