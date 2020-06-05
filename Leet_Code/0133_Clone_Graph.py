""" 133. Clone Graph

Question:

    Given a refernce of a node in a connected undirected graph.

    Return a deep copy of the graph.

+++

Solution:

    Use the hashmap structure to copy over the graph nodes as we are traversing
    on it.

"""

from collections import defaultdict

class Solution:
    def cloneGraph(self, node):
        if not node:
            return

        queue = [ node ]
        newRoot = Node(node.val, [])
        record = defaultdict(Node)
        record[node] = newRoot

        while queue:
            curr = queue.pop(0)
            for currNeighbour in curr.neighbours:
                # the neighbour may or may not be created beforehand.
                if currNeighbour not in record:
                    record[currNeighbour] = Node(currNeighbour.val, [])
                    queue.append(currNeighbour)
                record[curr].neighbours.append(record[currNeighbour])
        return newRoot # return new entry into clone'd graph.
