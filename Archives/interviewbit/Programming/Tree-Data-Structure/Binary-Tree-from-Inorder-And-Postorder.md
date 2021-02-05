# Binary Tree from Inorder And Postorder

    Given inorder and postorder traversal of a tree, construct the binary tree.

    Note: You may assume that duplicates do not exist in the tree. 


## Approach:

Here, we note that for every root value chosen from postorder traversal, its
left and right subtree is populated by the divided array where the root value
has been chosen.

Hence, we recursively traverse down; and at every depth, we choose top of
postorder traversal as our root for current subtree. Then, its left and right
subtree is populated by recursive call to updated inorder start and end
indicies determined by chosen value's index.

O(n) in time complexity.

---

Python:

```python

class Solution:

    def buildTree(self, inorder, postorder):

        def helper(l, r):
            if l > r:
                return None

            node = TreeNode(postorder.pop())

            if l == r:
                return node

            rootIdx = inorder.index(node.val)
            node.right = helper(rootIdx + 1, r)
            node.left = helper(l, rootIdx - 1)

            return node

        return helper(0, len(inorder) - 1)
```
