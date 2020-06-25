""" 4.3 List Of Depths


Question:

    Given a binary tree, design an algorithm which creates a linked list of all
    the nodes at each depth. (i.e. if you have a tree with depth D, you'll have
    D linked lists).

---

Among all the tree (graph) traversal algorithms, one that fits the description
would be the BFS, which traverses in level-order. The level order means that it
traverses through the tree depth by depth.

We can either assume that the treeNode that we have given also has next variable
for us to simply create the links of, or simply store the variables to create
the linked list when we are finished, or create one as we are traversing. In the
end, the time complexity should remain same except the difference in maybe the
temp storage issues.

"""

# assume LinkedList is available
import LinkedList

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def createLevelOrderList(self, root:TreeNode):
        if not root: return []
        result = [] # result is list[LinkedList]

        currentList = LinkedList()
        if root: currentList.add(root)
        while !currentList.isEmpty():
            result.add(currentList) # add prev level
            parents = currentList
            currentList = LinkstedList()
            for parent in parents:
                if parent.left: currentList.add(parent.left)
                if parent.right: currentList.add(parent.right)
        return result


