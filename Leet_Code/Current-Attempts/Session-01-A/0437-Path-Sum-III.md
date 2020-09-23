# 437 Path Sum III

Record the paths from "root" to the current node that we are visiting at the
moment. The number of paths that ends at the current node with the target sum
are counted.

---

Python:

```python

from collections import defaultdict

class Solution:
    def pathSum(self, root, target):
        def helper(node, partialPathSum):
            if not node: return 0

            partialPathSum += node.val
            count = paths[partialPathSum - target]

            paths[partialPathSum] += 1
            count += helper(node.left, partialPathSum)
            count += helper(node.right, partialPathSum)

            paths[partialPathSum] -= 1
            return count

        paths = defaultdict(int)
        paths[0] = 1

        return helper(root, 0)
```
