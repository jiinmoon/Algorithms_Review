# 105 Construct Binary Tree from Pre/Inorder Traversal
#
# The preorder traversal gives us hint at the order of nodes to visit; and for
# each node, its position in the inorder traversal will denote the nodes from
# left subtree and right subtree.

class Solution:
    def constructBT(self, preorder, inorder):
        def helper(prevNode):
            if not inorder or inorder[-1] == prevNode:
                return

            currNode = TreeNode(preorder.pop())
            currNode.left = helper(currNode.val)
            inorder.pop()
            currNode.right = helper(prevNode)
            return currNode
            
        preorder.reverse()
        inorder.reverse()
        return helper(None)
