113 Path Sum II
===============

Question:
---------

Given a binary tree and a sum, find all root-to-leaf paths where each path's
sum equals the given sum.

Solutions:
----------

We will explore all root-to-leaf paths while keeping track of the pathSum. If
at leaf node when we have our pathSum == 0, then we append our path to the
result array. This is a O(n * log(n)) algorithm since we are exploring down to
the tree's depth (log n).

Codes:
------

Python:

```python
class Solution:
    def pathSum(self, root, sum):
        results = []

        def dfs(node, path, pathSum):
            if not node:
                return
            if not pathSum - node.val and not node.left and not node.right:
                results.append(path + [node.val])
                return
            if node.left:
                dfs(node.left, path + [node.val], pathSum - node.val)
            if node.right:
                dfs(node.right, path + [node.val], pathSum - node.val)

        dfs(root, [], sum)
        return results
```

Go:

```go
func pathSum(root *TreeNode, sum int) [][]int {
    results := [][]int{}
    if root == nil {
        return results
    }
    if root.Left == nil && root.Right == nil {
        # early exit strategy
        if sum == root.Val {
            return append(results, []int{root.Val})
        }
        return results
    }
    for _, path := range pathSum(root.Left, sum - root.Val) {
        results = append(results, append([]int{root.Val}, path...))
    }
    for _, path := range pathSum(root.Right, sum - root.Val) {
        results = append(results, append([]int{root.Val}, path...))
    }
    return results
}
```

---

**Source:**

LeetCode: [Path-Sum-II](https://leetcode.com/problems/path-sum-ii/)
