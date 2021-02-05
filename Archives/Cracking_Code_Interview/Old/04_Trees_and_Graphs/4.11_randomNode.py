""" 4.11 Random Node


Question:

    You are implementing a binary searc htree class from scratch, which, in
    addition to insert, find, and delete, has a method getRandomNode() which
    returns a random node from the tree. All nodes should be equally likely to
    be chosen. Design and implement an algorithm for getRandomNode, and explain
    how you would implement the rest of the methods.

---

First intuition on implementing such algorithm is that leverage upon the fact
that this is a binary search tree; so long as we know the min and max range of
the tree, we can generate a random number, then try to find that number within
the tree if present; otherwise, find next closest number to it within the tree.

But let us explore few options:

1. One option is to simply convert the binary search tree into a list of
numbers, then return the random number from this array. While this would take
linear time, it would also take O(n) space. This is not optimal and most likely
to be too simplistic for our algorithm.

2. Label each nodes within the BST; then choose random number of label, and find
the label'd node within the tree. However, unless we have somehow kept the label
information from the scratch (in the implementaion of the BST), we will have to
spend O(N) time to label each of the nodes, thus, does not offer much increase
in time.

3. We approach the problem in terms of the probability. At each node, what is
the likelihood of returning its node value? It should be 1/N where N is the
total # of the nodes within the BST. The problem is this, at what probability
with should visit the left or right child if the current node is not chosen? The
intuition might be 50/50, but it is not. What if the left subtree has more nodes
than the right subtree? Then we will have to visit the left subtree more often
than the right subtree. Thus, it depends on the size of the subtrees at each
node as to where to visit in next level.

In order for option 3 to work as efficiently as possible, we will have to assume
that each node maintains its own sizes. This would be relatively easy to do so
if we are to implement the Tree from very scratch.

"""
import random

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.size = 1

    def getRandomNode(self):
        leftSize = self.left.size if self.left else 0

        index = random.randint(1, self.size)
        if index < leftSize:
            return self.left.getRandomNode()
        elif index == leftSize:
            return self
        else:
            return right.getRandomNode()

    def insertInorder(self, x):
        if x <= self.val:
            if not self.left:
                self.left = TreeNode(x)
            else:
                self.left.insertInorder(x)
        else:
            if not self.right:
                self.right = TreeNode(x)
            else:
                self.right.insertInorder(x)

