# 1345. Jump Game IV

Given an array of integers arr, you are initially positioned at the first index
of the array.

In one step you can jump from index i to index:

i + 1 where: i + 1 < arr.length.
i - 1 where: i - 1 >= 0.
j where: arr[i] == arr[j] and i != j.
Return the minimum number of steps to reach the last index of the array.

Notice that you can not jump outside of the array at any time.

---

There are multiple approaches, but finding shortest path from start at 0 to
goal of end of index can be found using either BFS or heuristic search
algorithm.

Here, we can use bidirectional bfs to avoid worst case scenario of continuously
exploring on the path with heavy branching factor.

For each node that we examine, we not only have to check for the neighbours
which are the cases of i+1 and i-1 but also the face that arr[i] is also in
arr[j]. To do this, we prepare an adjacency matrix where we are to collect the
indicies that belong under the same value.

The time complexity is O(n) to traverse on all nodes.

---

Python:

```python

class Solution:
    def jumpGame(self, nums):
        if len(nums) <= 2:
            return 0
        
        # collect indicies of same value in nums
        g = collections.defaultdict(list)
        for i, num in enumerate(nums):
            g[num].append(i)

        front, back, visited = {0}, {n-1}, set()
        jumps = 1

        while front:
            if len(front) > len(back):
                front, back = back, front

            newFront = set()

            for i in front:
                visited.add(i)

                # case: arr[i] == arr[j]
                for j in graph[nums[i]]:
                    if j in back:
                        return jumps
                    # visit each valid j positions
                    if j not in visited:
                        visited.add(j)
                        newFront.add(j)
i               
                # once visited, we do not have to search again on same positions
                graph.pop(nums[i])

                # case: i+1 and i-1
                for ni in [i+1, i-1]:
                    if ni in back:
                        return jumps
                    if 0 <= ni < len(nums) and ni not in visited:
                        visited.add(ni)
                        newFront.add(ni)
            
            front = newFront
            jumps += 1

        return -1
```
