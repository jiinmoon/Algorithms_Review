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

We can apply the definition of the BST: at each node its left val has to be
less than itself and right val has to be greater than itself. But we also have
to remember that this definition is applied recursively - not just at local
level. Hence, as we traverse down, we need to update our minimum and maximum
ancestor values to check our node for its valid range.

When we traverse to left, than all nodes in its left subtree has to be less
than current node's value. As well, when we traverse to right, then all nodes
in right subtree has to be greater.

Time complexity would be O(n) as we can complete this in a single traveral
through the tree. Space complexity of O(n) due to maintaining the recursive
stack call or iterative stack for nodes.

---

Python: recursive DFS approach.

```python

class Solution98:

    def isValidBST(self, root):

        def helper(node, minVal, maxVal):
            if not node:
                return True

            if node.val <= minVal or node.val >= maxVal:
                return False

            return helper(node.left, minVal, node.val) and helper(node.right, node.val, maxVal)


        return helper(root, float('-inf'), float('inf')
```

Python: iterative DFS approach.

```python

class Solution98:

    def isValidBST(self, root):

        if not root:
            return True

        stack = [(root, float('-inf'), float('inf'))]

        while stack:

            node, minVal, maxVal = stack.pop()

            if not node:
                continue

            if node.val <= minVal or node.val >= maxVal:
                return False

            stack.append((node.right, node.val, maxVal))
            stack.append((node.left, minVal, node.val))
        
        return True

```
