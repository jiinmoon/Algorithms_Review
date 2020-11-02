# 815 Bus Routes

We have a list of bus routes. Each routes[i] is a bus route that the i-th bus
repeats forever. For example if routes[0] = [1, 5, 7], this means that the
first bus (0-th indexed) travels in the sequence 1->5->7->1->5->7->1->...
forever.

We start at bus stop S (initially not on a bus), and we want to go to bus stop
T. Travelling by buses only, what is the least number of buses we must take to
reach our destination? Return -1 if it is not possible.

---

This problem can be viewed as a graph - and finding the shortest route from
S to T. To achieve this, we can use BFS (Bidirectional) to find the minimum
number of steps (or bus exchanges) required.

First, we create a mapping for each stop to their buses. From stop to stop, we
traverse to next possible reacheable stop by considering all buses running on
that stop. To avoid cycles, we maintain a visited set to track the already seen
stops. The time complexity should be bounded by the number of the stops to
explore.

---

Python:

```python

class Solution:
    def numBusesToDestination(self, routes, S, T):
        # set conversion in order for set operations to update the queue easily
        routes = [set(r) for r in routes]

        # neighbour of each stop to its list of buses that runs on this stop
        g = collections.defaultdict(set)
        for bus, stops in enumerate(routes):
            for stop in stops:
                g[stop].add(buss)

        f, b, visited = {S}, {T}, {}
        totalExchanges = 0

        while f and b and not (f & b):
            newf = set()
            for stop in stops:
                visited.add(stop)
                for bus in g[stop]:
                    newf |= routes[bus]
            f = newf - visited
            totalExchanges += 1
            if len(f) > len(b):
                f, b = b, f

        return totalExchanges if f & b else -1
```

