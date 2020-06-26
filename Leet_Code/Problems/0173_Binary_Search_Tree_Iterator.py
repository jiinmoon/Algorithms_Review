""" 173. BST Iterator

Question:

    Implement an iterator overa binary search tree where 'next()' will return
    the next smallest number in the BST.

+++

Solution:

    Since we are returning the values in the BST in sorted manner, we would like
    to traverse the tree in in-order fashion.

    When we have our iterator initialized, we would have a pointer wait at the
    leftmost node - in fact, this should be a function that can be called
    repeatedly.

    During initialization, we would find the leftmost node while maintaining the
    stack. When next() is called, we would simply return the top of the stack,
    while populate the stack again with current node's right subtree.

"""

class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self._findLeftmostNode(root)

    def _findLeftMostNode(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        currNode = self.stack.pop()
        self._findLeftMostNode(currNode)
        return currNode.val

    def hasNext(self):
        return len(stack) > 0
