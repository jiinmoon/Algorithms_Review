# Remove Half Nodes

Given a binary tree A with N nodes.

You have to remove all the half nodes and return the final binary tree.

NOTE:

Half nodes are nodes which have only one child.
Leaves should not be touched as they have both children as NULL.

---

To remove the "half" nodes, we skip over the nodes that which have a single
children. Once we arrive at non-half nodes, we adjust the pointers to left and
right by other non-half nodes found below.

O(n) in time complexity.

---

Python:

```python

class Solution:

    def removeHalfNodes(self, root):

        if not root:
            return None
        
        # traverse over nodes with single child
        while root:
            if root.left and not root.right:
                root = root.left
            elif not root.left and root.right:
                root = root.right
            else:
                break
        
        # first non-half node is found
        # reattach left and right subtree by next non-half nodes found below
        root.left = self.removeHalfNodes(root.left)
        root.right = self.removeHalfNode(root.right)

        return root
```
