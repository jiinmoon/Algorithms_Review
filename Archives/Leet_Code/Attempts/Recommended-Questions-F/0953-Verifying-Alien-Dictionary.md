# 953. Verifying Alien Dictionary

In an alien language, surprisingly they also use english lowercase letters, but
possibly in a different order. The order of the alphabet is some permutation of
lowercase letters.

Given a sequence of words written in the alien language, and the order of the
alphabet, return true if and only if the given words are sorted
lexicographicaly in this alien language.

---

From given "order" of characters, we can create its character to index mapping.
Thus, for each word that we examine, we create a mapping based on above
criteria - end result will be a list of indicies. Overall, all this resulting
lists should be in lexcographically sorted order. Since for each word, we need
to iterate on the word, the time complexity should be O(k * n) where k is the
length of the word and n is the number of words given.

---

Java:

```java

class Solution {
    
    public boolean isAlienSorted(String[] words, String order) {

        // create lexicographical order based on given alien dictionary
        int[] alien_dict = new int[26];
        for (int i = 0; i < order.length(); i++)
            alien_dict[order.charAt(i) - 'a'] = i;

        // check every pair of words for sorted order
        for (int i = 1; i < words.length+1; i++) {
            if (checkAlienOrder(words[i-1], words[i], alien_dict))
                return false;
        }
        return true;
    }
    
    public boolean checkAlienOrder(String word1, String word2, int[] dict) {
        // iterate forward comparing char by char and their mapped order in dict
        int i = 0;
        while (i < word1.length() && i < word2.length()) {
            int word1_order = dict[word1.charAt(i) - 'a'];
            int word2_order = dict[word2.charAt(i) - 'a'];
            
            if (word1_order == word2_order) {
                i++;
                continue;
            } else if (word1_order > word2_order) {
                return true;
            }

            return false;
        }
        // if terminated, all chars upto i has been matched
        // then, word1 size should be smaller than word2 at least
        return word1.length() > i;
    }
}

```

Python:

```python

class Solution:
    def isAlienSorted(self, words, order):
        order = {i:char for i, char in enumerate(order)}
        prevMapping = list()
        for word in words:
            currMapping = [order[char] for char in word]
            if prevMapping >= currMapping:
                return False
            prevMapping = currMapping
        return True
```
