""" 105. Construct BT from Preorder and Inorder Traversal

Question:

    Given preorder and inorder traversal of a tree, construct the binary tree.

+++

Solution:

    From the preorder, we can choose our current node. And from the inorder, we
    can find the current node's left and right subtrees.

"""

class Solution:
    def buildTree(self, preorder, inorder):
        if len(inorder) == len(preorder) == 0:
            return None

        curr = TreeNode(preorder[0])
        inorderIDX = inorder.index(curr.val)

        curr.left = self.buildTree(preorder[1:inorderIDX+1], inorder[:inorderIDX])
        curr.right = self.buildTree(preorder[inorderIDX+1:],
                inorder[inorderIDX+1:])
        return curr
