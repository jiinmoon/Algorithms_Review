863 All Nodes Distance K in Binary Tree
=======================================

We are given a binary tree (with root node root), a target node, and an integer
value K.

Return a list of the values of all nodes that have a distance K from the target
node.  The answer can be returned in any order.

---

We can perform DFS to find the target node; and at the target, we go down
K steps to find all the nodes of K dist from the target. Problem now is finding
the Kth node from the target that may lie in another subtree. To do so, we need
to find the subtree that does not contain the target node.

---

Python:

```python
class Solution:
    def distanceK(self, root, target, K):
        res = []

        def findNodesAtDist(node, dist):
            if not node: return
            if dist == 0:
                res.append(node.val)
            else:
                findNodesAtDist(node.left, dist - 1)
                findNodesAtDist(node.right, dist - 1)

        def dfs(node):
            if not node: return -1
            if node == target:
                findNodesAtDist(node, K)
                return 0    # indicate target is found at this subtree
            l, r = dfs(node.left), dfs(node.right)
            # if both are -1, then no target found down below at this node
            if l == r == -1:
                return -1
            # update distance to target
            distToTarget = 1 + max(l, r)
            if K - distToTarget == 0:
                findNodesAtDist(node, 0)
            elif K - distToTarget > 0:
                # find nodes at subtree that does not contain target
                otherSide = node.left if l == -1 else node.right
                findNodesAtDist(otherSide, K - distToTarget - 1)
            return distToTarget

        dfs(root)
        return res
```
