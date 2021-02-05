# Inorder Traversal

Given a binary tree, return the inorder traversal of its nodes’ values.

---

Recursive solution is trivial; iterative solution involves using stack to
append nodes while we traverse as far left as possible on each of the nodes.
When we finished visiting the current node, we move onto its right.

O(n) in time complexity.

---

Python:

```python

class Solution:

    def inorderTraversal(self, root):

        if not root:
            return []

        result, stack = [], []

        while root or stack:

            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            result.append(root.val)
            root = root.right

        return result
```
