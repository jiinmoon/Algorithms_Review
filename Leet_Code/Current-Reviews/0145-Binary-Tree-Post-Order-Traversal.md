# 145. Binary Tree Postorder Traversal

Given the root of a binary tree, return the postorder traversal of its nodes'
values.

---

Python: Recursive.

```python

class Solution:

    def postorderTraversal(self, root):

        def traverse(node):
            if node:
                traverse(node.left)
                traverse(node.right)
                result.append(node.val)

        result = []

        traverse(root)

        return result
```

Python: Iterative.

```python

class Solution:

    def postorderTraversal(self, root):

        stack, result = [root], []

        while stack:

            curr = stack.pop()

            if curr:
                
                result.append(curr.val)

                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)

        return result[::-1]
```
