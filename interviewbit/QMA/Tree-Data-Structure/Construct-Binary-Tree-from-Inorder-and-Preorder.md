# Contruct Binray Tree from Inorder and Preorder

Given preorder and inorder traversal of a tree, construct the binary tree.

---

We can recursively build binary tree by taking top of preorder as our root of
the subtree; then, left subtree is populated by values found to inorder that is
left of the target preorder root value and vice versa. O(n) in time complexity.

---

Python:

```python

class Solution:

    def buildTree(self, preorder, inorder):

        preorder = preorder.reverse()
        inorder = inorder.reverse()

        def _build(stop):
            if not inorder or inorder[-1] == stop:
                return None

            node = TreeNode(preorder.pop())
            node.left = _build(node.val)
            inorder.pop()
            node.right = _build(stop)

            return node

        return _build(None)

```
