218 The Skyline Problem
=======================

A city's skyline is the outer contour of the silhouette formed by all the
buildings in that city when viewed from a distance. Suppose giventhe locations
and height of all the buildings, write a progrm to output the skyline formed by
these buildings collecively.

---

We will be given the list of buildings by its left point and right point on
X axis as well as its height on y axis. Firstable, we will collect all the left
and right points from the buildings as well as their associated building's
height and sort them first by its edges in increasing order then heights in
reverse.

We will maintain a heap of heights and right edge so that it will maintain the
highest point in the given set of buildings that are within the same range.
Thus, so long as the edges that we exaimne has greater left edge than what is
already in the top of heap, then we can safely pop off from the heap.
Otherwise, we first take a look at the height - if it is not 0 then we can push
into the heap.

After updating the heap, if the current have changed compared to what is in the
result (i.e. new building silhouette found) then we add to the result.


Time complexity should be O(n * log(n)) due to sorting involved.

---

Python:

```python
import heapq

class Solution:
    def getSkyline(self, buildings):
        result = [ (0,0) ]
        # max heap (first by height, then right point)
        currentBuildings = [ (0, float('inf')) ]

        # record all left and right edges
        allEdges = list()
        for left, right, height in buildings:
            allEdges.append( (left, -height, right) )
            # right edges are identified with 0 height
            allEdges.append( (right, 0, None) )

        for pt, height, right in allEdges:
            # update current set of buildings
            # if top of buildings right point is less than current point
            # no need to maintain it, pop.
            while currentBuildings[0][1] <= pt:
                heappop(currentBuilds)

            # if current edge is not right point but left, then we add to the
            # current building to build the skyline
            if h != 0:
                heappush(currentBuildings, (h, r))

            # update the result
            # if the max height of the leftmost point in the current building
            # is not same as what was exaimned previously, then new skyline
            if result[-1][1] != -heap[0][0]:
                result.append( [e, -heap[0][0]] )

        return result[1:]
```
