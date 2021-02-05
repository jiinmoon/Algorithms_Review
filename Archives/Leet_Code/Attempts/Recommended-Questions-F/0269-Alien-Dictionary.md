# 269. Alien Dictionary

There is a new alien language which uses the latin alphabet. However, the order
among letters are unknown to you. You receive a list of non-empty words from
the dictionary, where words are sorted lexicographically by the rules of this
new language. Derive the order of letters in this language.

---

This problem can be approached as a graph problem where we would perform dfs as
far as possible on individual unique characters where edges are formed between
the characters that comes after to before.

For this problem, we first prepare a graph in the form of adjacency martrix. We
collect individual unique characters and determine the adjacency by comparing
two adjacent words. We take a look at each of the characters from the two
words. If they characters are not same, then this potentially tells us about
the order - we record that current character has neighbour of previous.
However, here we have to also check for whether the words are valid; if the
previous word is a prefix of another word starting from where the character is
not same, the order is impossible and we can early exit.

Then we perform dfs on each individual nodes; at each node, we visit all the
neighbours. However, at any point, we determine that we return to the same
node, current order should be discarded as it means that character that has
started the path has appeared before the later one.

The time complexity in general should be O(n) where n is the length of the
characters represented as we do not have to revisit each but only once to
determined their status of visitation.

---

Java:

```java

class Solution {
    
    public String alienDictionary(String[] words) {

        // create a graph and a counter of unique characters
        // graph tracks the toplogical direction of characters
        // indegree tracks the inward edges towards nodes
        Map<Character, List<Character>> graph = new HashMap<>();
        Map<Character, Integer> indegree = new HashMap<>();

        for (String word : words) {
            for (char c : word.toCharArray()) {
                graph.put(c, new LinkedList<>());
                indegree.put(c, 0);
            }
        }

        // find edges; unique chars differ at each index points from prev to curr
        for (int i = 1; i < word.length; i++) {
            String prev = words[i-1];
            String curr = words[i];
            
            for (int j = 0; j < Math.min(prev.length(), curr.length()); j++) {
                if (prev.charAt(j) != curr.charAt(j)) {
                    // previous char points to current char
                    graph.get(prev.charAt(j)).add(curr.charAt(j));
                    // increase degree of current char
                    indegree.put(curr.charAt(j), indegree.get(curr.charAt(j) + 1));
                    break;
                }
            }
            
            // think of cases such as "qkts" -> "qk"
            if (prev.length() > curr.length() && prev.startsWith(curr))
                return "";
        }
        
        // perform toplogical traversal
        // start from all nodes with no indegree edges
        StringBuilder result = new StringBuilder();
        Deque<Character> q = new LinkedList<>();
        for (char c : indegree.keySet()) {
            if (indegree.get(c) == 0) q.add(c);
        }

        while (!q.isEmpty()) {
            char curr = q.remove();
            // current is all visited; safe to add to result
            result.append(curr);
            for (char neighbour : graph.get(curr)) {
                // update neighbour; it is visited and decrease its indegree count
                indegree.put(neighbour, indegree.get(neighbour) - 1);
                if (indegree.get(neighbour) == 0)
                    q.add(neighbour);
            }
        }
        
        // after finished visiting all nodes, we should have no indegrees leftover 

        return (counts.values().stream().mapToInt(i->i.intValue()).sum() == 0) ?
            result.toString() : "";
    }
}

```

Python:

```python

class Solution:
    def alienDictionary(self, words):
        # move down as far as cycle is detected
        def helper(node):
            if node in visited:
                return visited[node] # if cycle returns False

            visited[node] = False
            for neigh in d[node]:
                haveVisited = helper(neigh) # cycled detected?
                if not haveVisited:
                    return False
            
            # finished all paths from this
            # build order
            visited[node] = True
            result.append(node)
            return True

        # create a adjacency list
        d = {c:[] for word in words for c in word}

        # create edges between words in order
        for prev, curr in zip(words, words[1:]):
            for c1, c2 in zip(prev, curr):
                # discrepency is where order would be
                if c1 != c2:
                    d[c2].append(c1)
                    break
            else:
                if len(prev) > len(curr):
                    return ""
        
        visited = set()
        result = list()
        
        # every node should be visited without cycle
        if not any(helper(node) for node in d.keys()):
            return ""
        return "".join(result)
```
