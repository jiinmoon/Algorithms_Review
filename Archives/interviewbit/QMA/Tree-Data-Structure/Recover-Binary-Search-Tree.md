# Recover Binary Search Tree

Two elements of a binary search tree (BST) are swapped by mistake.

Tell us the 2 values swapping which the tree will be restored.

A solution using O(n) space is pretty straight forward. Could you devise
a constant space solution? 

---

Inorder traveral on the Binary Search Tree will find us the two values which
are out of the order. We could iterate once and find them which costs us O(n)
in space. Better approach would be to maintain the previous node as we perform
the inorder traversal.

---

Python:

```python

class Solution:

    def recoverTree(self, root):

        prev, swapped1, swapped2 = TreeNode('-inf'), None, None

        def _inorder(node):

            nonlocal prev, swapped1, swapped2     

            if node:

                inorder(node.left)
                
                # previous node is out of order
                if node.val <= prev.val:
                    # set to 1 if it is first
                    if not swapped1:
                        swapped1 = prev
                    # set to 2 if it is second
                    if swapped1:
                        swapped2 = node
                
                prev = node

                inorder(node.right)

        _inorder(root)

        return [swapped2, swapped1]
```
