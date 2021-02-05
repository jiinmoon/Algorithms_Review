# Inorder Traversal of Cartesian Tree

    Given an inorder traversal of a cartesian tree, construct the tree.

    
    Cartesian tree : is a heap ordered binary tree, where the root is greater than
    all the elements in the subtree. 
    
    Note: You may assume that duplicates do not exist in the tree. 


---

## Approach:

One approach would be to repeatedly find the maximum value as the current root
of the tree, and populate left and right by the dividing the given inorder list
from where the maximum value has been found. This would be O(n^2) in time
complexity due to having to linearly search for the maximum value and its index
at every recursion depth.

Improvement can be made by utilizing the heap; for every node that we examine,
we compare against the top of the stack. So long as top of our stack is
smaller, we try to maintain the larger nodes in the stack by removing from top
of the stack. Then, we append current node which is found to be smaller than
top of the stack as a right subtree, and attach the last node removed which is
found to be smaller than the current on the left. And add current node back
into the stack. This will be O(n) in time and space complexity.

---

Python: Stack approach.

```python

class Solution:

    def buildTree(self, inorder):

        stack = []

        for val in inorder:

            prev, node = None, TreeNode(val)

            while stack and stack[-1] < val:
                prev = stack.pop()

            if stack:
                stack[-1].right = node

            if prev:
                node.left = prev

            stack.append(node)

            prev = None

        return stack[0]

```

Python: Recursive linear search for max value approach.

```python

class Solution:

    def buildTree(self, inorder):
        
        if not inorder:
            return None

        maxVal, maxIdx = 0, 0

        for i, num in enumerate(inorder):
            if maxVal < num:
                maxVal = num
                maxIdx = i

        node = TreeNode(maxVal)
        node.left = self.buildTree(inorder[:maxIdx])
        node.right = self.buildTree(inorder[maxIdx + 1:])
        
        return node

```
