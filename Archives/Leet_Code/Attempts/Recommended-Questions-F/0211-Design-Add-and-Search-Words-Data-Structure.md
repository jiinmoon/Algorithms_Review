# 211. Design Add and Search Words Data Structure

Design a data structure that supports adding new words and finding if a string
matches any previously added string.

Implement the WordDictionary class:

```
WordDictionary() Initializes the object.

void addWord(word) Adds word to the data structure, it can be matched later.

bool search(word) Returns true if there is any string in the data structure
that matches word or false otherwise. word may contain dots '.' where dots can
be matched with any letter.
```

---

To implement this structure, we can approach in two ways - one is using Trie
and other is hashmap by length of the given word. Both approach has its cons
and pros. The later approach will be constant in adding a new word, but will
require a linear search that is based on the count of the words inserted with
matching the count of the word.

---

Java: Trie apprach.

```java

class WordDictionary {

    static class TrieNode {
        Map<Character, TrieNode> children;
        String word;

        public TrieNode() {
            this.children = new HashMap<>();
            this.word = null;
        }
    }
    
    TrieNode root;

    public WordDictionary() {
        this.root = new TrieNode();
    }

    public void add(String word) {
        TrieNode curr = this.root;
        for (char c : word.toCharArray()) {
            TrieNode next = curr.getOrDefault(c, new TrieNode());
            curr.put(c, next);
            curr = next;
        }
        curr.word = word;
    }

    public boolean search(String word) {
        Deque<TrieNode> q = new LinkedList<>(List.of(this.root));
        for (char c : word.toCharArray()) {
            Deque<TrieNode> temp = new LinkedLIst<>();
            for (TrieNode curr : q) {
                if (c == '.') 
                    temp.addAll(curr.children.values());
                else if (curr.children.containsKey(c))
                    temp.add(curr.children.get(c));
            }
            if (temp.isEmpty())
                return false;
            q = temp;
        }

        for (TrieNode node : q) {
            if (node.word != null)
                return true;
        }

        return false;
    }
}

```

Java: length of word approach:

```java

class WordDictionary {
    
    Map<Integer, List<String>> dict;

    public WordDictionary() { this.dict = new HashMap<>(); }

    public void add(String word) {
        List<String> neighbours = this.dict.getOrDefault(word.length(), new LinkedList<>());
        neighbours.add(word);
        this.dict.put(word.length(), neighbours);
    }

    public boolean search(String word) {
        List<String> neighbours = this.dict.getOrDefault(word.length(), new LinkedList<>());
        for (String target : neighbours) {
            int i = 0;
            while (i < Math.min(target.length(), word.length())) {
                if (word.charAt(i) == '.' || word.charAt(i) == target.charAt(i)) i++;
                else break;
            }
            if (i == Math.min(target.length(), word.length())) return true;
        }
        return false;
    }
}

```

Python:

```python

class WordDictionary:
    def __init__(self):
        self.d = collections.defaultdict(list)

    def addWord(self, word):
        self.d[len(word)].append(word)

    def search(self, word):
        for target in self.d[len(word)]:
            for i, char in enumerate(target):
                if word[i] != "." and word[i] != char:
                    break
            else:
                return True
        return False
```
