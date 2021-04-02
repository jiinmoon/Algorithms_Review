# 105. Construct Tree from Preorder and Inorder Traversal

Given two integer arrays preorder and inorder where preorder is the preorder
traversal of a binary tree and inorder is the inorder traversal of the same
tree, construct and return the binary tree.

---

Inorder traversal of the given binary tree reveals the how a chosen element
node will have a its subtree values to its left and right. In other words, for
any chosen element in inorder list, the values to its left and its left subtree
and vice versa until the root boundary is found.

The root boundary chosen would be determined by the preorder list. Simple
iteration on the preorder list gives us what root values to choose as we build
the tree in preorder fashion. Hence, we continuously go down to the bottom of
our new tree until we have no more elements left in the inorder list or reached
the end of our boundary. At each depth, we choose our current root node from
the preorder list; and its left subtree would be populated by recursive call to
itself while setting the boundary to stop at the chosen root value form the
inorder list. Once we return finished building left subtree, then we repeat the
process on the right - but we must not forget that current inorder value is
same as the root value; hence we should remove from our inorder list.

---

Python:

```python

class Solution105:

    def buildTree(self, preorder, inorder):

        preorder.reverse()
        inorder.reverse()

        def build(stop):
            if not inorder or inorder[-1] == stop:
                return None

            currNode = preorder.pop()
            # left is populated upto currently selected root value from preorder
            currNode.left = build(currNode.val)
            # remove current root value from inorder and repeat on right
            inorder.pop()
            # right subtree is populated upto current iteration's stop value
            currNode.right = build(stop)
            return currNode

        return build(None)
```
