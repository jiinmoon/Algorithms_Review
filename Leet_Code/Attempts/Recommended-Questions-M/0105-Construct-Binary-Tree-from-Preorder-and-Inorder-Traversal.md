# 105. Construct Binary Tree from Preorder and Inorder Traversal

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:

You may assume that duplicates do not exist in the tree.

---

When we exaimne the preorder traversal list, we notice that this gives us
a current node values as we build the binary tree if we are to approach this in
preorder method. And when we do so, the chosen current node value in inorder
traversal reveals that elements to be popluate to its left and right subtrees.
Hence, when we recurisve build the tree in preorder fashion, we can stop
building down at the path where the inorder element has reached the previously
chosen node value.

Since we only have to iterate once on the given list, the time complexity
should be of O(n).

---

Python:

```python

class Solution:
    def buildTree(self, preorder, inorder):
        def helper(marker):
            if not inorder or inorder[-1] == marker:
                return None

            currVal = preorder.pop()
            currNode = TreeNode(currVal)
            # go left until we exhuast all elements to left of marker in inorder
            currNode.left = helper(currVal)
            # remove marker
            inorder.pop()
            # repeat the same on right subtree, carrying over marker
            currNode.right = helper(marker)
            return currNode
        
        # operate from end of the list (O(1))
        preorder = preorder[::-1]
        inorder = inorder[::-1]
        return self.helper(None)
```

