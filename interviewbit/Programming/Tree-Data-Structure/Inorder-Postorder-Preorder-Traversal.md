# Pre/In/Postorder Traversal

Implement Pre/In/Postorder Traversal algorithsm iteratively.

---

Python:

```python

class Solution:

    def preorderTraversal(self, root):

        if not root:
            return []

        stack, result = [root], []

        while stack:

            curr = stack.pop()

            if curr:
                result.append(curr.val)

                stack.append(curr.right)
                stack.append(curr.left)
        
        return result


    def inorderTraversal(self, root):

        if not root:
            return []

        stack, result = [], []

        while root or stack:

            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            result.append(root.val)
            root = root.right

        return result


    def postorderTraversal(self, root):

        if not root:
            return []

        stack, result = [], [root]

        while stack:

            curr = stack.pop()

            if curr:
                result.append(curr.val)

                stack.append(curr.left)
                stack.append(curr.right)

        return result[::-1]
```
