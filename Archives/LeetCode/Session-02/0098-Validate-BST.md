# 98. Validate BST

Given the root of a binary tree, determine if it is a valid binary search tree
(BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's
key.

The right subtree of a node contains only nodes with keys greater than the
node's key.

Both the left and right subtrees must also be binary search trees.

---

To check for whether given binary tree is a valid binary search tree or not, we
can traverse on each node, and check whether it falls within the correct range;
which is that all the nodes to the left has to contain values less than its
parent and vice versa.

But the definition has to apply recursively to all subtrees within the binary
tree - hence, whenever we traverse on the tree, we have to update our range.

---

Python:

```python

class Solution98:

    def isValidBSTRecur(self, root):

        def helper(node, minV, maxV):
            if not node:
                return True
            if node.val <= minV or node.val >= maxV:
                return False
            return helper(node.left, minV, node.val) and helper(node.right, node.val, maxV)

        return helper(root, float('-inf'), float('inf')

    def isValidBSTIter(self, root):

        if not root:
            return True

        queue = [(root, float('-inf'), float('inf')]

        while queue:

            temp = list()
            
            for node, minV, maxV in queue:
                if node.val <= minV or node.val >= maxV:
                    return False
                if node.left:
                    temp.append( (node.left, minV, node.val) )
                    temp.append( (node.right, node.val, maxV) )

            queue = temp

        return True
```
