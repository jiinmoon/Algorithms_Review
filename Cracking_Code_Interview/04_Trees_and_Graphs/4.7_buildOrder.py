""" 4.7 Build Order


Question:

    You are given a list of projects and a list of dependencies which is a list
    of pairs of proects, where the second project is dependent on the first
    project. All of a project's dependencies must be built before the project
    is. Find a build order that will allow the projects to be built. If there is
    no valid build order, return an error.

Example:

    input:

        projects: a, b, c, d, e, f
        dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)

    Output:

        f, e, a b, d, c

---

This is a dependency problem, that we can think of as a graph problem. Reimagine
the problem in a directed graph where each nodes represents the projects and the
edges represent the dependencies that must happen. Then, by traversing through
from one node to another, we can find the valid order of traversal.

Start with a node that does not have any inbound edges. Then, we remove the
outbound edges of the nodes. Repeat the process until we have exhausted the pool
of nodes that we have to go through.

Alternatively, we can repeatedly perform DFS on any of the nodes to find the
topological sort on the graph.

"""
