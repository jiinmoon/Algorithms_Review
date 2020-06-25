""" 501. Find Mode in BST

Question:

    Find all values that appear most frequent in a BST that allows duplicates.

+++

Solution:

    As we iterate on the BST, we will count each of the elements. Then, we will
    see which count is the highest, and return all those which have count equal
    to highest.

"""

from collections import defaultdict


class Solution:
    def findModes(self, root):
        if not root:
            return []

        counter = defaultdict(int)
        queue = [ root ]
        maxCount = 0
        while queue:
            curr = queue.pop(0)
            counter[curr] += 1
            maxCount = max(maxCount, counter[curr])
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        result = [ k for k, v in counter.items() if v == maxCount ]
        return result
