# Inorder Traveral of Cartesian Tree

Given an inorder traveral of a cartesian tree, construct tree.

 Cartesian tree : is a heap ordered binary tree, where the root is greater than
 all the elements in the subtree. 

---

We recursively build the tree where each node is the current maximum of the
given inorder array. Then, all values to the left of maximum is used to
populate the left subtree and vice versa on the right subtree.

---

Python:

```python

class Solution:

    def buildTree(self, inorder):

        if not inorder:
            return None

        maxVal, maxIdx = 0, 0
        for i in range(len(inorder)):
            if maxVal < inorder[i]:
                maxVal = inorder[i]
                maxIdx = i

        node = TreeNode(maxVal)
        node.left = self.buildTree(inorder[:maxIdx])
        node.right = self.buildTree(inorder[maxIdx + 1:])

        return node

```
