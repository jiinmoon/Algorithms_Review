545 Boundary of Binary Tree
===========================

Given a binary tree, return the values of its boundary in **anti-clockwise**
direction starting from root. The boundary includes left boundary, leaves, and
right boundary in order without duplicate nodes.

---

We approach this problem in different traverses on the given binary tree. We
will perform preorder traversal on the left side and right side of the binary
tree to gather all the in-path boundary on the left and right.

As for the leaves, we perform inorder traversal on the left and right side:
when we arrive at leaf, we append it to our boundary.

Time complexity should be linear as it should take 4 traversals in total
(traverse down on left and right; inorder traversal on left and right).

---

Python:

```python

class Solution:
    def boundaryOfBinaryTree(self, root):
        # move down on left side to gather left boundary nodes
        def traverseLeft(node):
            if not node or not(node.left or node.right):
                return
            lBound.append(node.val)
            if node.left:
                traverseLeft(node.left)
            else:
                traverseLeft(node.right)
        
        # reverse of above
        def traverseRight(node):
            if not node or not(node.left or node.right):
                return
            rBound.append(node.val)
            if node.right:
                traverseRight(node.right)
            else:
                traverseRight(node.left)

        # inorder traversal to gather all leaves
        def traverseInorder(node):
            if not node:
                return
            traverseInorder(node.left)
            if not node or not(node.left or node.right):
                lBound.append(node.val)
            traverseInorder(node.right)

        if not root:
            return list()

        lBound, rBound = list(), list()

        traverseLeft(root.left)
        traverseInorder(root.left)
        traverseInorder(root.right)
        traverseRight(root.right)

        return [root.val] + lBound + rBound[::-1]
```

