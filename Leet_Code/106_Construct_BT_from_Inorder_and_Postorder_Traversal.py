""" 106. Construct BT from Inorder and Postorder Traversal """

class Solution:
    def buildTree(self, inorder, postorder):
        if len(inorder) == len(postorder) == 0:
            return None

        curr = TreeNode(postorder.pop())
        inorderIDX = inorder.index(curr.val)

        curr.left = self.buildTree(inorder[:inoderIDX], postorder[:inorderIDX])
        curr.right = self.buildTree(inorder[inorderIDX+1:],
                postorder[inorderIDX:])

        return curr
