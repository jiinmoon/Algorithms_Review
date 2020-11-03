# 437. Path Sum III

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go
downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range
-1,000,000 to 1,000,000.

---

As we traverse down on the given binary tree, we maintain the partial path sum.
By using a record of partial path sums and the number of path count that has
such paths, we can easily find the total count in recursive manner.

---

Python:

```python

class Solution:
    def pathSum(self, root, sum):
        def helper(node, partialSum):
            if not node:
                return 0
            
            partialSum += node.val
            count = d[partialSum - sum]

            # update path count by 1
            # when we explore different path, decrease the record by 1
            d[partialSum] += 1
            count += helper(node.left, partialSum)
            count += helper(node.right, partialSum)
            d[partialSum] -= 1
            return count
        d = collections.defaultdict(int)
        d[0] = 1
        return helper(root, 0)
```


