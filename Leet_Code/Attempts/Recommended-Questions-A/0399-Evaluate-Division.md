# 399. Evaluate Division

You are given an array of variable pairs equations and an array of real numbers
values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai
/ Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth
query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined,
return -1.0.

Note: The input is always valid. You may assume that evaluating the queries
will not result in division by zero and that there is no contradiction.

---

We visualize this problem as a graph problem where each node represents value
and directed edge is created with a weight that computes the division operation
from node A to node B (A/B). Then, it is about finding all the connected paths
and its weights using the Floyd-Warshall algorithm. The time complexity would
be O(n^3).

---

Java:

```java

class Solution {

    public double[] calcEquations(List<List<String>> equations, double[] values, List<List<String>> queries)
    {
        // map equations[i][j] to 2D array; assign node number
        // i.e. A / B is assigned a node number 0
        int m = equations.size(), nodeNum = 0;
        int[][] eqMatrix = new int[m][2];
        Map<String, Integer> eqMap = new HashMap<>();

        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < m; j++)
            {
                String node = equations.get(i).get(j);
                if (eqMap.contains(node)) {
                    eqMatrix[i][j] = eqMap.get(node);
                } else {
                    eqMatrix[i][j] = nodeNum;
                    eqMap.put(node, nodeNum);
                }
            }
        }
        
        // create adjcency matrix
        double[][] adjMatrix = new double[nodeNum][nodeNum];

        for (int i = 0; i < m; i++)
        {
            // A / A = 1
            adjMatrix[i][i] = 1;
            // A / B = val 
            adjMatrix[eqMatrix[i][0]][eqMatrix[i][1]] = values[i];
            // B / A = 1 / val
            adjMatrix[eqMatrix[i][1]][eqMatrix[i][0]] = values[i];
        }

        // floyd-warshall; iterate to compute possible pairings
        for (int A = 0; A < nodeNum; A++)
        {
            for (int B = 0; B < nodeNum; B++)
            {
                for (int C = 0; C < nodeNum; C++)
                {
                    if (adjMatrix[B][C] == 0 && adjMatrix[B][A] != 0 && adjMatrix[A][C] != 0) {
                        // B / C = B / A * A / C
                        adjMatrix[B][C] = adjMatrix[B][A] * adjMatrix[A][C];
                        adjMatrix[C][B] = 1 / adjMatrix[B][C];
                    }
                }
            }
        }

        // collect queries
        double[] result = new double[queries.size()];

        for (int i = 0; i < queries.size(); i++)
        {
            String A = queries.get(i).get(0);
            String B = queries.get(i).get(1);

            if (eqMap.containsKey(A) && eqMap.containsKey(B)
                result[i] = adjMatrix[eqMap.get(A)][eqMap.get(B)];
            result[i] = (result[i] == 0) ? -1 : result[i];
        }
        
        return result;
    }
}

```

Python:

```python

class Solution:
    def calcEquation(self, equations, values, queries):
        graph = collections.defaultdict(dict)
        for i in range(len(equations)):
            src, dst, val = equations[i][0], equations[i][1], values[i]
            graph[src][dst] = val
            graph[dst][src] = 1/val

        for A in graph:
            for B in graph[A]:
                for C in graph[A]:
                    # B/C = B/A * A/C
                    graph[B][C] = graph[B][A] * graph[A][C]

        result = list()
        for src, dst in queries:
            if src in graph and dst in graph[src]:
                result.append(graph[src][dst])
            else:
                result.append(-1.0)

        return result
```
