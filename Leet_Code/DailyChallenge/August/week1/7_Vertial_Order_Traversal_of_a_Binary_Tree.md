# LeetCode Daily Challenge: August Week.1 - Day.7

## Question

Given a binary tree, return the vertical order traversal of its nodes values.

For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).

Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes, we report the values of the nodes in order from top to bottom (decreasing Y coordinates).

If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.

Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.

## Solution

First, iterate on the given binary tree and retrieve the mapping between (x, y)
coordinates of each nodes and the values. When we traverse to left, (x-1, y-1),
and to right, (x+1, y-1).

Then, we will have a map where we can sort by its key which is the x values.
But also, we need to sort by the y in decending order as well for each
x coordinate values.

Python:

```python
from collections import defaultdict

class Solution:
    def verticalTraversal(self, root):
        res = []
        xyMap = defaultdict(list)
        
        def traverse(node, x, y):
            if not node:
                return
            xyMap[x].append((-y, node.val)) # -y for sort decending order
            traverse(node.left, x-1, y-1)
            traverse(node.right, x+1, y-1)

        traverse(root, 0, 0)
        # sort by x coords
        sortedXYMap = sorted(xyMap.keys())
        for x in sortedXYMap:
            # sort by y in decending order
            xyMap[x].sort()
            res.append([v for _, v in xyMap[x]])
        return res
```
