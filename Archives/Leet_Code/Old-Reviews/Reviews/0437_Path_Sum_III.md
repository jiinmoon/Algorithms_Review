437 Path Sum III
================

Question:
---------

Given a binary tree, find number of all paths that sum to target value. The paths is not necessarily a root-to-leaf path.

Solutions:
----------

Naive approach would be to start traversal from each node until pathSum is
reached or we go above. This is O(n^2) approach which can be improved further
by using memoization.

Another way to approach this problem is to consider root to any node path sum.
If there was a solution within this path, that it must have been old
root-to-node pathSum such that (currSum - oldSum). 

We will simply maintain a dictionary that will track the number of paths from
root to node that has target sum. Increment the count of the current path and
recursive on left and right.

The dictionary will contain its key the sum of path from the root; and its
value will be the count of such paths.

Time and space complexity is O(n).

Codes:
------

Python:

```python
from collections import defaultdict

class Solution:
    def pathSum(self, root, sum):
        paths = defaultdict(int)
        paths[0] = 1 # default; there is 1 path == 0 pathSum

        def traverse(node, pathSum):
            if not node:
                return 0

            pathSum += node.val
            # count is the number of paths that ends in current node
            count = paths[pathSum - sum]
            # record path ending at current node
            paths[pathSum] += 1
            # recursve on left and right to find total count
            count += traverse(node.left, pathSum)
            count ++ traverse(node.right, pathSum)
            # prepare for next recursion
            paths[pathSum] -= 1
            return count

        return traverse(root, 0)
```

---

**Source:**

LeetCode: [Path-Sum-III](https://leetcode.com/problems/path-sum-iii/)
