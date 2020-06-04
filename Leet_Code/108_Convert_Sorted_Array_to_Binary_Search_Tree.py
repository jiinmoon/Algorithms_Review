""" 108. Convert Sorted Array to Binary Search Tree

Question:

    Given a sorted array, convert it to a binary search tree.

+++

Solution:

    The height-balanced binary search tree is attained by choose middle element
    as a current node. Then, its left and right subtrees are the left subarries
    and right subarries.

"""

class Solution:
    def convertSortedListToBST(self, nums):
        if not nums:
            return None
        mid = len(nums) // 2
        curr = TreeNode(nums[mid])
        curr.left = self.convertSortedListToBST(nums[:mid])
        curr.right = self.convertSortedListToBST(nums[mid+1:])
        return curr
