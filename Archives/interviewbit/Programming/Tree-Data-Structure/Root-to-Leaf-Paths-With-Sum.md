# Root to Leaf Paths With Sum

    Given a binary tree and a sum, find all root-to-leaf paths where each
    path’s sum equals the given sum.


---

## Approach:

Recursively traverse down to the leaf node whilst building the path of nodes
that have seen thus far. If the path sum has reached the given sum, we can add
our path to the result.

O(n) in time complexity.

---

Python:

```python

class Solution:

    def pathSum(self, root, target):

        def helper(node, path, pathSum):

            if not node:
                return
            
            if not (node.left or node.right):
                if pathSum + node.val == target:
                    result.append(path + [node.val])
                return

            helper(node.left, path + [node.val], pathSum + node.val)
            helper(node.right, path + [node.val], pathSum + node.val)

        result = []

        helper(node, [], 0)

        return result
```
