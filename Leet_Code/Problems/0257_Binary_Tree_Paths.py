""" 257. Binary Tree Paths """

class Solution:
    def binaryTreePaths(self, root):
        result = []

        def traverse(node, path):
            if not node:
                return
            if not node.left and not node.right:
                result.append('->'.join(path))
                return
            if node.left:
                traverse(node.left, path + [str(node.val)])
            if node.right:
                traverse(node.right, path + [str(node.val)])

        traverse(root, [])
        return result
