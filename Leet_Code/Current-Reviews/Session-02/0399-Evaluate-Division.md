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
{   A : { B = X
    B : { C = Y

```
