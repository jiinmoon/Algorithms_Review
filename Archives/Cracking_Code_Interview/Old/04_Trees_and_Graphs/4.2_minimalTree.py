""" 4.2 Minimal Tree


Question:

    Given a sorted (increasing order) array with unique integer elements, write
    an algorithm to create a binary search tree with minimal height.

---

The questions asks to create a height-balanced BST given the 'sorted' array.
Here, we note that one of the properties of the BST is that its left-to-right
order, that is in-order traversal of BST element is exactly the sorted order of
the its Nodes' elements.

Thus, we have the following: we choose the mid element from the sorted array.
Then, all the elements less than mid element should be on the left and vice
versa. This implies that with the chosen mid element as a parent, all the left
elements belong under left subtree and vice versa.

As the binary tree (BST) is recursive in nature, the definition should apply
recursively down to last element in the array.

"""

class GraphNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def createMinBst(self, nums: List[int]):
        return self._createMinBst(self, nums, 0, len(nums)-1)

    def _createMinBst(self, nums: List[int], start:int, end:int):
        if end < start: return None

        # find mid value
        mid = (start + end) // 2

        # create new node
        newNode = GraphNode(nums[mid])

        # repeat recursively on left half and right half
        newNode.left = self._createMinBst(nums, start, mid - 1)
        newNode.right = self._createMinBst(nums, mid + 1, end)

        return newNode


