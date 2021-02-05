""" 210. Course Shcedule II """

# only changes are that we now need to return the list of path that takes to
# complete all the courses; simply, whenever we visit the node, we can add to
# the result list since the fact that we have visited the course refers to that
# we have completed the pre-reqs for that course.

from collections import defaultdict

class Solution:
    def findOrder(self, numCourses, prereqs):
        result = []
        neighbours = defaultdict(list)
        inDegrees = [0] * numCourses
        queue = []
        depth = 0 # to simply maintain whether we complete.

        # populate neighbours list and inDegrees from prereqs.
        for course, prereq in prereqs:
            neighbour[prereq].append(course)
            inDegrees[course] += 1

        # find indegree 0 course to start.
        for course in range(numCourses):
            if not inDegree[course]:
                queue.append(course)

        # start topological sort.
        while queue:
            curr = queue.pop(0)
            result.append(curr)
            depth += 1
            for neighbour in neighbours[curr]:
                inDegrees[neighbour] -= 1
                if not inDegrees[neighbour]:
                    queue.append(neighbour)

        return result if depth == numCorses else []

