399 Evaluate Division
=====================

Equations are given in the format A / B = k, where A and B are variables
represented as strings, and k is a real number (floating point number). Given
some queries, return the answers. If the answer does not exist, return -1.0.

---

We think of this problem as a graph problem: each verticies will contain the
varaibles, and directed edge between two verticies are the value of division v1
/ v2. Then, we can repeatedly find all the rechable edges and its weight using
Floyd-Warshall algorithm for finding shortest paths in weighted graph.

The graph is represented as a hashmap of hashmap - src node to dst node are the
numerator of the equation to denomenator of the equation where its edge weight
is the value of its division expression.

For example, if we have A / B = K, then the graph will represent it as
{ A : { B : K } }. Since it is also possible to go from B to A, we can also
reflect it on the graph by updating it to { A: { B : K }, B : { A : 1/K } }.

Suppose that we have A / B = X and B / C = Y. Initial graph will look as
follows:

```
{   
    A : { B : X },
    B : { A : 1/X , C : Y },
    C : { B : 1/Y }
}
```

Now, we need to evaluate every varaible against each other to explore the
missing edges. For A, B, C in the outer loop, we consider every B and C in the
expression such that:

```
graph[A][C] = graph[A][B] * graph[B][C] = X / Y

which is equivalent to

A/C = A/B * B/C
```

Due to having to explore all nodes, and all other edges in every direction each
time, the time complexity as O(V^3) for number of verticies in graph.

---

Python: Floyd-Warshall algorithm.

```python
from collections import defaultdict

class Solution:
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(dict)
        for i in range(len(equations)):
            numer, denom, value = equations[i][0], equations[i][1], values[i]
            # src -> dst is { numer : { denom : value } }
            graph[numer][denom] = value
            # dst -> src :
            # denom = numer / value
            # so it is { denom : { numer : 1/value } }
            graph[denom][numer] = 1 / value

        # complete all possible paths and compute the unfilled divisions
        # for A node, pick every other B and C
        for A in range(graph):
            for B in range(graph[a]):
                for C in range(graph[a]):
                    # B/C = B/A * A/C
                    graph[B][C] = graph[B][A] * graph[A][C]

        res = list()
        for numer, denom in queries:
            if numer in graph and denom in graph[numer]:
                res.append(graph[numer][denom])
            else:
                res.append(-1.0)

        return res
```

