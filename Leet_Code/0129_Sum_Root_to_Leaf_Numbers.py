""" 129. Sum Root to Leaf Numbers

Question:

    Given a binary tree containing digits from 0-9 only, each root-to-leaf path
    coul represent a number.

    Find the total sum of all root-to-leaf numbers.

+++

Solution:

    We traverse down to leafs, exploring all paths leading to it. Then, at leaf
    nodes, we append to result list the number representing that path.

"""

class Solution:
    def sumNumbers(self, root):
        if not root:
            return []

        result = []

        def traverse(node, path):
            if not node.left and not node.right:
                result.append(path + node.val)
                return
            if node.left:
                traverse(node.left, (path + node.val) * 10)
            if node.right:
                traverse(node.right, (path + node.val) * 10)

        traverse(root, 0)
        return sum(result)
