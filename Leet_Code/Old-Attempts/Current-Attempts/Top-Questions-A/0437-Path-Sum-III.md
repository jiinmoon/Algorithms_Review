# 437 Path Sum III

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go
downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range
-1,000,000 to 1,000,000.

---

The naive approach would be to repeatedly perform a downward traversal from
each of the nodes to confirm whether it will make a path sum to a given value.
To repeat O(n) traversal on n number of nodes will be O(n^2) in time
complexity.

Better approach would be to record the number of paths of the prefix sum of the
current paths. So that we carry partial sum of the paths that we are on, and
count this partial path sum minus the target sum.

This is achieved with a hashmap that maintains the count of the paths from the
root to the each of the nodes in the tree. This approach would be O(n) in
time complexity as well as in space.

---

Python:

```python

class Solution:
    def pathSum(self, root, targetSum):
        def helper(node, partialSum):
            if not node:
                return 0

            partialSum += node.val
            pathCount = g[partialSum - targetSum]
            
            # record current prefix sum
            g[partialSum] += 1
            # total count to be returned from both subtrees
            pathCount += helper(node.left, partialSum)
            pathCount += helper(node.right, partialSum)
            g[partialSum] -= 1
            
            return pathCount

        g = collections.defaultdict(int)
        # base case; there are 1 path with sum 0
        g[0] = 1
        return helper(root, 0)
```
