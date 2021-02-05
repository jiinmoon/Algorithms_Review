94 Binary Tree Inorder Traversal
================================

Question:
---------

Given a binary tree, implement inorder traversal in iterative fashion.

Solutions:
----------

A typical DFS algorithm involving a stack can be used to iterate in O(n).

Codes:
------

Python:

```python
class Solution:
    def inorderTraversal(self, root):
        if not root:
            return
        stack, result = [], []
        while root:
            stack.append(root)
            root = root.left
        while stack:
            curr = stack.pop()
            result.append(curr.val)
            if curr.right:
                curr = curr.right
                while curr:
                    stack.append(curr)
                    curr = curr.left
        return result
```

Go:

```go
func pop(stack []*TreeNode) (*TreeNode, []*TreeNode) {
    end := len(stack)-1
    return stack[end], stack[:end]
}

func inorderTraversal(root *TreeNode) []int {
    var (
        stack []*TreeNode{}
        result []int
    )
    for curr := root; curr != nil || len(stack) != 0; {
        for curr != nil {
            stack = append(stack, curr)
            curr = curr.Left
        }
        curr, stack = pop(stack)
        result = append(result, curr.Val)
        curr = curr.Right
    }
    return result
}
```

---

**Source:**

LeetCode: [Binary-Tree-Inorder-Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)
