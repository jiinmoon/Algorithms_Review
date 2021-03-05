# 94. Binary Tree Inorder Traversal

Given the root of a binary tree, return the inorder traversal of its nodes'
values.

---

The recursive solution is rather trivial. Hence, iterative approach would be
worth exploring here. To iteratively traverse the binary tree in "inorder"
fashion, we require stack. First, for every node, we have to explore as far to
the leftmost node as possible - while saving the node for revisit in the stack.
Once we have arrived at the leftmost node, this will be revisited and can be
recorded as our inorder result. If there are right subtree to this visited
node, the process is repeated.

---

Python:

```python

class Solution94:

    def inorderIter(self, root):

        stk, result = [], []

        while root or stk:

            while root:
                stk.append(root)
                root = root.left

            root = stk.pop()

            if root:
                result.append(root.val)
                root = root.right
        
        return result


    def inorderRecur(self, root):
        
        def helper(node):
            if not node:
                return

            helper(node.left)
            result.append(node.val)
            helper(node.right)

        result = []
        helper(root)

        return result
```
