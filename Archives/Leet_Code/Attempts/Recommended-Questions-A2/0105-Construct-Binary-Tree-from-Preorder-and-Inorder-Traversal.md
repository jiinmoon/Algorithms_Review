# 105. Construct Binary Tree from Preorder and Inorder Traversal

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

---

We can recursively build our tree in preorder fashion using the preorder; every
element in the preorder becomes the new node at each depth. To determine how
far we should go, we should take a look at the inorder. Inorder tells us that
which nodes are poluated to the current node's left and right subtrees; hence,
we know when to stop by examining the inorder list.

---

Python:

```python

class Solution105:

    def constructTree(self, preorder, inorder):
        
        def build(stop):
            # inorder is all used or have reached right end
            if not inorder or inorder[-1] == stop:
                return None

            # preorder traversal; current node is top of preorder
            curr = TreeNode(preorder.pop())
            # left subtree is to the left of current val in inorder list
            curr.left = build(curr.val)
            # inorder visited; remove
            inorder.pop()
            # right subtree is to the end of previous stop
            curr.right = build(stop)

            return curr

        preorder.reverse()
        inorder.reverse()

        return build(None)
```

