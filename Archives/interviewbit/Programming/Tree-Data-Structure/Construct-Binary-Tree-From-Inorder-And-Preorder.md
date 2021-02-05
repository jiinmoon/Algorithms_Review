# Construct Binary Tree From Inorder And Preorder

    Given preorder and inorder traversal of a tree, construct the binary tree.

    Note: You may assume that duplicates do not exist in the tree. 


## Approach:

For every preorder root value chosen, its left and right subtree is populated
by the left and right divided array pivoted by the chosen preorder root value.

O(n) in time complexity.


---

Python:

```python

class Solution:

    def buildTree(self, preorder, inorder):

        def helper(stop):
            if not inorder or inorder[-1] == stop:
                return None

            node = TreeNode(preorder.pop())
            node.left = helper(node.val)
            inorder.pop()
            node.right = helper(stop)
            return node

        preorder.reverse()
        inorder.reverse()

        return helper(None)
```


