# 315. Count of Smaller Numbers After Self

You are given an integer array nums and you have to return a new counts array.
The counts array has the property where counts[i] is the number of smaller
elements to the right of nums[i].

---

The main problem here is that we need to constantly iterate on the previous
result count list in order to update all the values that are less than the
current value; this nested solution will result in time complexity of O(n^2) or
worse.

The potentially improved solution would be using the binary search tree where
each nodes are modified to maintain the count of nodes belonging to its left
subtree. As insertion is log(n) process, the time complexity may reduced
further down to O(n * log(n)).

---

Python:

```python

# modified tree node to maintain count of left subtree
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.leftCount = 0
        self.l, self.r = None, None

class Solution:
    def countSmaller(self, nums):
        result = [0] * len(nums)

        if len(nums) < 2:
            return result

        # starting from behind
        # treat last value as the root of the BST
        # perform insertion for every value to follow
        root = TreeNode(nums[-1])
        for i in range(len(nums)-2, -1, -1):
            curr = root
            leftCount = 0
            
            # insertion process continues until position is found
            while True:
                # current node's value is greater than insertion value
                # current node's leftCount is incremented and move to left of curr
                if nums[i] < curr.val: 
                    curr.leftCount += 1
                    # first check to see insertion point is reached
                    # if empty, insertion point is found
                    if not curr.left:
                        curr.left = TreeNode(nums[i])
                        break
                    else:
                        curr = curr.left
                # otherwise, we need to move to right
                # the left subtree count has to be maintained
                # it is incremented by the amount of left subtree count of curr
                else:
                    leftCount += curr.leftCount
                    # it is possible that it is a duplicate
                    # if not, we also need to increment further by 1
                    if nums[i] > curr.val:
                        leftCount += 1
                    if not curr.right:
                        curr.right = TreeNode(nums[i])
                        break
                    else:
                        curr = curr.right

            # finished insertion; record the left subtree count
            result[i] = leftCount

        return result
```
