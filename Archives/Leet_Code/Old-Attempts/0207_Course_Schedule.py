""" 207. Course Schedule

Question:

    Given courses and pre-reqs, can you finished the courses?

+++

Solution:

    This problem can be seen as a graph problem - in particular this would be a
    topological sort problem. Hence, we can use BFS to solve it. However, the
    tweak here is that we need to find the entry point into the graph; and that
    entry point are the nodes where they do not have a pre-req.

"""

from collections import defaultdict

class Solution:
    def canFinish(self, numCourses, prereqs):
        neighbours = defaultdict(list)
        inEdges = [0] * numCourses
        # prereqs is List[List[int]], convert.
        for x, y in prereqs:
            neighbours[y].append(x)
            inEdges[x] += 1
        # start with nodes with indegree of 0.
        queue = [ i for i inrange(numCourses) if inEdges[i] == 0 ]
        while queue:
            curr = queue.pop(0)
            for neighbour in neighbours[curr]:
                inEdges[neighbour] -= 1
                # if the node has no longer any indegrees, then it is safe.
                if inEdges[neighbour] == 0:
                    queue.append(neighbour)
        return sum(inEdges) == 0 # complete if no nodes have prereqs left.
