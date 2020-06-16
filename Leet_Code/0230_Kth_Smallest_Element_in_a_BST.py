""" 230. Kth Smallest Element in a BST """

from collections import deque

class Solution:
    def findKthSmallest(self, root, k):
        # iterative DFS approach.
        if not root:
            return
        stack = deque()
        curr = root
        while curr or stack:
            # continusouly going to left on each new curr node.
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if k == 1:
                return curr.val
            curr = curr.right
            k -= 1
