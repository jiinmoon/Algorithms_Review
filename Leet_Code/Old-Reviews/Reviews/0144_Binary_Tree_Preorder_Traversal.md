144 Binary Tree Preorder Traversal
==================================

Question:
---------

Given a binary tree, return the _preorder_ traversal of its nodes' values.

Solutions:
----------

Since recusive algorithm is trivial, we would like to solve it using iterative
approach. Here, we use DFS algorithm with stack to explore the tree. The result
is populated whenever we encounter a new node.

Codes:
------

Python:

```python
class Solution:
    def preorderTraversal(self, root):
        if not root:
            return []

        result = []
        stack = [ root ]
        while stack:
            curr = stack.pop()
            result.append(curr.val)
            # think recursively (or stack wise)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return result
```

Go:

```go
type nodeStack struct {
    stack []*TreeNode
}

func (s *nodeStack) push(node *TreeNode) {
    s.stack = append(s.stack, node)
}

func (s *nodeStack) pop() (node *TreeNode, []*TreeNode) {
    if s.isEmpty {
        return
    }
    end := len(s.stack)-1
    return s.stack[end], s.stack[:end]
}

func (s *nodeStack) isEmpty() bool {
    return len(s.stack) == 0
}

func preorderTraversal(root *TreeNode) []int {
    var (
        result = []int{}
        s = nodeStack{}
        curr = &TreeNode
    )
    if root == nil {
        return result
    }
    s.push(root)
    for !s.isEmpty() {
        curr, s.stack = s.pop()
        result = append(result, curr.Val)
        if curr.Right != nil {
            stack.push(curr)
        }
        if curr.Left != nil {
            stack.push(curr)
        }
    }
    return result
}
```
---

**Source:**

LeetCode: [Binary-Tree-Preorder-Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal)
