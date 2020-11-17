# 269. Alien Dictionary

There is a new alien language which uses the latin alphabet. However, the order
among letters are unknown to you. You receive a list of non-empty words from
the dictionary, where words are sorted lexicographically by the rules of this
new language. Derive the order of letters in this language.

---

The relative ordering of the characters are determined diagonally downwards if
we are to visualize it. Then, to find the complete ordering of this letters, we
take a look at two words at a time and their composition. A character that
appears in later word and mismatched with the character from the same position
from previous word signals the ordering. This creates an edge between the nodes
where we can traverse as far out as possible to determine the order.

However, while we are traversing, if the character "does not" returns back to
the previously visited node, this means that current path is invalid - which
means that there does "not" exist any meaningful solution overall.

Hence, the problem boils down to first creating a graph, where nodes are
characters and edges form between nodes if they are connected by same position
on the previous word and not same. Then, traversing as far out as possible to
detect a cycle. For each node, if we find that we can return to previous, then
our ordering is valid and can be formed.

The time complexiy should be O(n).

Let's take a look at an example:

```
Suppose that we are given list of "wrt", "wrf", "er", "ett", "rftt". The
relative order that we can tell is "w, r, t, f, e" but not complete.

By examining this list, we can first create our directed graph such as follows:

    w <- e <- r <- t <- f

So, let's perform traversal as far out as possible on each of these nodes.

dfs(w) will return True and mark "w" as visited; and terminate further as no
connecting nodes. The "w" is our starting order.

dfs(r) finds neighbour "e". dfs(e) further down will also call for dfs(w). But
since "w" has been marked visited, it will return True. So, "e" is added to
result, and subsequently returns True to last dfs(r). Now, "r" is addd and
returns True.

dfs(t) has neighbour "r". But we have "r" already visited before; hence, it is
valid and "t" is marked and added to result.

dfs(f) has neighbour "t" which is same as above. The path downwards from dfs(t)
has been explored previously and is in order.

dfs(e) back to "w" closes the loop;

Hence, our result should be ["w", "e", "r", "t", "f"].

At any moment, if a node traverses to unvisited node, then it cannot form
order.
```

---

Python:

```python

class Solution:
    def alienDictionary(self, words):
        # gather all unqiue characters in order
        graph = {c : list() for c in word for word in words}
        # form edges by comparing prev and current words
        # first characters that does not agree tells the order
        # however, if second word length is smaller, order is impossible
        for prev, curr in zip(words, words[1:]):
            for c1, c2 in zip(prev, curr):
                if c1 != c2:
                    graph[c2].append(c1)
                    break
            else:
                if len(prev) > len(curr):
                    return ""

        visited = set()
        result = list()

        # detect cycle while building order
        def dfs(node):
            # node may have been visited before; propagate up
            if node in visited:
                return visited[node]

            visited[node] = False
            for neigh in graph[node]:
                prev = helper(neigh)
                if not prev:
                    return False
            visited[node] = True
            result.append(node)
            return True

        if not(any(dfs(node) for node in graph)):
            return ""

        return "".join(result)
```


