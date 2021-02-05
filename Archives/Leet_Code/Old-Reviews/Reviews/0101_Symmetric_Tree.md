101 Symmetric Tree
==================

Question:
---------

Given a binary tree, check whether it is a mirror of itself.

Solutions:
----------

We will trave on the same tree at two entries. We will traverse both at the
same time but one will move in opposite direction of the another to "mirror"
others movement down the tree.

Codes:
------

Go:

```go
func checkSymmetry(p, q *TreeNode) bool {
    if p == nil || q == nil {
        return p == nil && q == nil
    }
    if p.Val != q.Val {
        return false
    }
    return checkSymmetry(p.Left, q.Right) && checkSymmetry(p.Right, q.Left)
}

func isSymmetric(root *TreeNode) bool {
    if root == nil {
        return true
    }
    return checkSymmetry(root.Left, root.Right)
}
```

---

**Source:**

LeetCode: [Symmetric-Tree](https://leetcode.com/problems/symmetric-tree)
