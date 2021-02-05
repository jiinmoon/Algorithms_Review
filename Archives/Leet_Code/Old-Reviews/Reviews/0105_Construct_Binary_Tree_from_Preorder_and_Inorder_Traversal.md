105 Construct Binary Tree from Preorder and Inorder Traversal
=============================================================

Question:
---------

Given preorder and inorder traversal of a tree, construct the binary tree.

Solutions:
----------

The hint comes from the fact that when we iterate on the tree, preorder will
give us the current node that we are encountering. The first element of the
preorder will be the root and if we look at its position in inorder, then we
find that it actually divides the array such that it can be used to populate
the left and right subtrees. Thus, the process would be first pick the first
element of the preorder as our current node. And recursively build current
node's left and right subtrees by updating preorder and inroder lists. This
would be O(n) time complexity algorithm.

Codes:
------

Python: updating lists approach.

```python
class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder and not inorder:
            return None
        curr = TreeNode(preorder[0])
        inorderIdx = inorder.index(curr.val)

        curr.left = self.builTree(preorder[1:inorderIdx+1], inorder[:inorderIdx])
        curr.right = self.buildTree(preorder[inorderIdx+1:], inorder[inorderIdx+1:])
        return curr
```

Python: build left first until inorder idx of curr.val is reached.

```python
class Solution:
    def buildTree(self, preorder, inorder):
        preorder.reverse() # could have used deque() instead
        inorder.reverse()

        def build(stopVal):
            if not inorder or inorder[-1] == stopVal:
                return None
            # build left until root.val is encountered in inorder
            curr = TreeNode(preorder.pop())
            curr.left = build(curr.val)
            # inorder[-1] is prev curr.val
            inorder.pop()
            curr.right = build(stopVal)
            return curr
        return build(None)
```

---

**Source:**

LeetCode: [Construct-Binary-Tree-from-Preorder-and-Inorder-Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal)
