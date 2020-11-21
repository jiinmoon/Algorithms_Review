# 127. Word Ladder

Given two words (beginWord and endWord), and a dictionary's word list, find the
length of shortest transformation sequence from beginWord to endWord, such
that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.

Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.

---

We visualize this problem as a graph where we are trying to find a shortest
path between start to goal. Each node in the graph would be given words, and
nodes form edges among themselves if they are "1" edit distance away or can
transform according to the given criteria.

Here, we can use BFS (Bi-directional BFS) to find the shortest path. We use set
to compute the intersection between our frontiers. If two nodes overlap, the
paths have conjoined and we can return the length thus far.

Bidirectional BFS has a time complexity of O(d ^ (b/2)) where d is the number
of nodes (or distance) and b is the branching factor (how severe the out going
edges are there in nodes). Since we require to create a graph, space complexity
would be O(n).

---

Java:

```java

import java.util.HashSet;

class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        Set<String> words, front, back, visited;
        words = new HashSet<>(wordList);
        
        if (!words.contains(endWord)) return 0;
        
        // two frontiers from start and from goal
        front = new HashSet<>(List.of(beginWord));
        back = new HashSet<>(List.of(endWord));

        Map<String, Set<String>> graph = new HashMap<>();
        for (String word : words) {
            for (int i = 0; i < word.length(); i++) {
                String wild = word.substring(0, i) + "." + word.substring(i+1);
                Set<String> neighbours = graph.getOrDefault(wild, new HashSet<>());
                neighbours.add(word);
                graph.put(wild, neighbours);
            }
        }
        
        int length = 1;
        while (!front.isEmpty()) {
            // check intersection
            Set<String> result = new HashSet<>(front);
            result.retainAll(back);
            if (!result.isEmpty) return length;

            // swap to explore on smaller frontier
            if (front.size() > back.size()) {
                Set<String> temp = front;
                front = back;
                back = temp;
            }

            Set<String> nextFront = new HashSet<>();
            for (String word : front) {
                visited.add(word);
                for (int i = 0; i < word.length(); i++) {
                    String wild = word.substring(0, i) + "." + word.substring(i+1);
                    Set<String> neighbours = graph.getOrDefault(wild, new HashSet<>());
                    neighbours.removeAll(visited);
                    nextFront.addAll(neighbours);
                }
            }
            
            front = new HashSet<>(nextFront);
            length += 1;
        }

        return 0;
    }
}

```

Python:

```python

class Solution:
    def wordLadder(self, begin, end, words):
        words = set(words)
        if end not in words: return 0

        front, back, visited = {begin}, {end}, {}

        g = collections.defaultdict(list)
        for word in words:
            for i in range(len(word)):
                wild = word[:i] + "." + word[i+1:]
                g[wild].append(word)

        length = 1
        while front:
            if front & back:
                return length

            if len(front) > len(back):
                front, back = back, front

            nextFront = set()
            for word in front:
                visited.add(word)
                for i in range(len(word)):
                    wild = word[:i] + "." + word[i+1:]
                    nextFront |= g[wild] - visited

            front = nextFront
            length += 1

        return 0
```
