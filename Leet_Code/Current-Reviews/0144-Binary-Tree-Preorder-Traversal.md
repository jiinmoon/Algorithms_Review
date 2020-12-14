# 144. Binary Tree Preorder Traversal

Given the root of a binary tree, return the preorder traversal of its nodes'
values.

---

Python: Recursive.

```python

class Solution:

    def preorder(self, root):

        result = []

        def _traverse(node):
            if node:
                result.append(node.val)
                _traverse(node.left)
                _traverse(node.right)

        return result

```

Python: Iterative.

```python

class Solution:

    def preorder(self, root):

        stack, result = [root], []

        while stack:

            curr = stack.pop()

            if curr:
                result.append(curr.val)

                if curr.right:
                    stack.append(curr.right)
                if curr.left:
                    stack.append(curr.left)

        return result
```
