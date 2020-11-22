# 49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the
answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different
word or phrase, typically using all the original letters exactly once.

---

We can use the hashmap structure to map each of the sorted word to its list of
words that shares same sorted word. The time complexity would be 
O(k \* (n \* log(n))) where n is the length of the longest word and k is the
number of the words to group. The space complexity would be O(n) for words that
we record to return.

---

Java:

```java

import java.util.HashMap;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> m = new HashMap<>();
        for (String word : words) {
            // sort the word
            char[] temp = word.toCharArray();
            Arrays.sort(temp);
            String sortedWord = new String(temp);

            List<String> words = m.getOrDefault(sortedWord, new LinkedList<>());
            words.add(word);
            m.put(sortedWord, words);
        }

        return new LinkedList<>(m.values());
    }
}

```

Python:

```python

class Solution:
    def groupAnagrams(self, words):
        d = collections.defaultdict(list)
        for word in words:
            d[tuple(sorted(word))].append(word)
        return list(d.values())
```
