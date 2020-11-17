# 863. All Nodes Distance K in Binary Tree

We are given a binary tree (with root node root), a target node, and an integer
value K.

Return a list of the values of all nodes that have a distance K from the target
node.  The answer can be returned in any order.

---

We can easily find the nodes at distance k that are "below" the target node by
simply traversing downwards starting from the target. However, the problem is
that the distance to cover can go above the target node and through the
parents in the path.

We solve this problem by determining whether left or right subtree contains
the target node. If so, we can have it return 0; otherwise, -1. This would be
used as an indicator as to at each parent node, we determine the "other"
subtree where the target node has not been found to explore while updating our
distance as such.

Suppose that target node is reached and it returns 0 to our parent. The target
node is to left of our parent. Then, we can conclude that we can traverse on
our right subtree. Or, it could be the case that parent itself is at the Kth
distance from the target node.

The time complexity of this problem would be O(n) as well as its space
complexity.

---

Python:

```python

class Solution:
    def findAllNodesDistanceK(self, root, target, k):
        # simple search down from target node
        def searchdown(node, d):
            if not node: return
            if not d:
                result.append(node.val)
                return
            searchdown(node.left, d - 1)
            searchdown(node.right, d - 1)

        # dfs first to find the target node
        # at each node, determine whether target node lies on its left
        # or right subtree; if the update distance to cover still remains,
        # start search downward from the parent node on opposite from where
        # target node is found; or parent itself may be the one
        def dfs(node):
            if not node: return -1
            if target == node:
                searchdown(node, k)
                return 0
            l, r = dfs(node.left), dfs(node.right)
            if l == r == -1: return -1
            
            # we are at parent; distance increases by 1
            updatedDist = k - 1 + max(l, r)
            
            # parent itself is at k distance from target
            if updatedDist == 0:
                result.append(node.val)
            # parent's left or right subtree detected target node
            # start searching on other side
            elif updatedDist > 0:
                otherSide = node.left if l == -1 else node.right
                # -1 on dist since we already move one click
                searchdown(otherSide, updatedDist - 1)
            
            # otherwise, we continue upwards on parent path
            return updatedDist

        result = list()
        dfs(root)

        return result
```
