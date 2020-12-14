# 94. Binary Tree Inorder Traversal

Given the root of a binary tree, return the inorder traversal of its nodes'
values.

---

Python: Recursive.

```python

class Solution:

    def inorderTraversal(self, root):

        def traverse(node):

            if node:
                traverse(node.left)
                result.append(node.val)
                traverse(node.right)

        result = []

        traverse(root)

        return result
```

Python: Iterative.

```python

class Solution:

    def inorderTraversal(self, root):

        stack, result = [], []

        while root or stack:

            while root:
                stack.append(root)
                root = root.left

            curr = stack.pop()

            if curr:
                result.append(curr.val)
                curr = curr.right

        return result
```
