# 437. Path Sum III

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go
downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range
-1,000,000 to 1,000,000.

---

The problem arises from the fact that the path does not have to start from root
and end in leaf - but it also does need to go downwards, not through the node
to continue to another side of subtree.

We think of this problem as a finding continuous subarray sum to a given value.
Each path downward will be regarded as a continuous subarray - and we record
the partial or "prefix" sum as we recursively move downwards. Then, at each
node, we can find the count of whether current path sum has been reached by
checking against the record of previous prefix sums found along that path.

Both time and space complexity should be O(n) since we need to visit each nodes
and record the current path sum.

---

Python:

```python

class Solution:
    def pathSum(self, root, target):
        def dfs(node, pathSum):
            if not node: return 0
            pathSum += node.val
            count += d[pathSum - target]
            # before moving down, record current path
            d[pathSum] += 1
            count += dfs(node.left, pathSum)
            count += dfs(node.right, pathSum)
            # paths from current node are finished
            # delete so that it does not appear on another path
            d[pathSum] -= 1
            return count

        d = collections.defaultdict(int)
        d[0] = 1
        return dfs(root, 0)
```
