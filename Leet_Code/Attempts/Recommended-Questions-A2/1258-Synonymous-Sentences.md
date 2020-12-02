# 1258. Synonymous Sentences

Given a list of pairs of equivalent words synonyms and a sentence text, Return
all possible synonymous sentences sorted lexicographically.

---

First major difficulty would be finding all connected synonyms (connected
componenets) in the given pairs (or edges). Here, we use union find algorithm
to group all the connected synonyms.

Then, we can use BFS algorithm to generate all sentences for all words iterated
which are mapped to synonyms.

Since the sentences are to be sorted, time complexity is at least O(n
* log(n)).

---

Python:

```python

class Solution1258:

    def generateSentences(self, synonyms, text):

        def unionFind(word):
            if word not in union:
                union[word] = word
            while union[word] != word:
                word = union[word]
            return word

        # union-find structure
        union = dict()

        for word1, word2 in synonyms:
            union[unionFind(word1)] = unionFind(word2)

        # create a mapping of parent word to list of synonyms under that parent
        graph = collections.defaultdict(list)
        for word in union:
            graph[unionFind(word)].append(word)

        # bfs
        queue = [[""]]
        for word in text.split(" "):
            temp = list()
            neighbours = graph.get(unionFind(word), [word])
            for neigh in neighbours:
                for node in queue:
                    temp.append(node.copy() + [neigh])
            queue = temp
        
        # lexicographically sorted
        return [" ".join(node[1:]) for node in sorted(queue)]
```
