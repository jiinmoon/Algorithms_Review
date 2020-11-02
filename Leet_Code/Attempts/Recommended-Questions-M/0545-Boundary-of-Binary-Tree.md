# 545. Boundary of Binary Tree

Given a binary tree, return the values of its boundary in anti-clockwise
direction starting from root. Boundary includes left boundary, leaves, and
right boundary in order without duplicate nodes.  (The values of the nodes may
still be duplicates.)

Left boundary is defined as the path from root to the left-most node. Right
boundary is defined as the path from root to the right-most node. If the root
doesn't have left subtree or right subtree, then the root itself is left
boundary or right boundary. Note this definition only applies to the input
binary tree, and not applies to any subtrees.

The left-most node is defined as a leaf node you could reach when you always
firstly travel to the left subtree if exists. If not, travel to the right
subtree. Repeat until you reach a leaf node.

The right-most node is also defined by the same way with left and right
exchanged.

---

This requires a several different traversal algorithms to gather all the
boundary nodes. First, we want to gather all the left boundary nodes. We may do
this with recursive preorder algorithm that moves down on the left subtree
until we have reached the end. Then, we need to gather all the leaf nodes at
the bottom - to do so, we use the inorder traversal. And finally for the right
most boundary nodes, we use reversed algorithm of the first where we would
instead traverse on the right subtree instead of left.

---

Python:

```python

class Solution:
    def boundaryOfBinaryTree(self, root):
        def gatherLeftBoundary(node):
            if not node or not (node.left or node.right):
                return
            lBound.append(node.val)
            if node.left:
                gatherLeftBoundary(node.left)
            else:
                gatherLeftBoundary(node.right)

        def gatherRightBoundary(node):
            if not node or not (node.left or node.right):
                return
            rBound.append(node.val)
            if node.right:
                gatherRightBoundary(node.right)
            else:
                gatherRightBoundary(node.left)

        def gatherLeaves(node):
            if not node:
                return
            gatherLeaves(node.left)
            # reached leaf
            if not (node.left or node.right):
                lBound.append(node.val)
            gatherLeaves(node.right)

        if not root:
            return []

        lBound, rBound = [root.val], []
        gatherLeftBoundary(root.left)
        gatherLeaves(root.left)
        gatherLeaves(root.right)
        gatherRightBoundary(root.right)

        return lBound + rBound[::-1]
```
