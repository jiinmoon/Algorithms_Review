# 472. Concatenated Words

Given a list of words (without duplicates), please write a program that returns
all concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely of at
least two shorter words in the given array.

---

We first breakdown the given word at all possible points to generate prefix and
suffixes. For each suffixes, we recursive check for whether the suffixes
themselves are composed of the concatenated words. Since there composition of
word is fixed, we can use memoization to save work.

---

Java:

```java

class Solution {

    HashMap<String, Boolean> memo;

    public List<String> findAllConcatenatedWords(String[] words)
    {
        if (words == null || words.length == 0)
            return new ArrayList<>();

        HashSet<String> dict = new HashSet<>();
        for (String word : words)
            dict.add(word);

        List<String> result = new ArrayList<>();
        for (String word : words)
        {
            dict.remove(word);
            if (helper(word, dict))
                result.add(word);
            dict.add(word);
        }

        return result;
    }
    
    public boolean helper(String s, Set<String> dict)
    {
        if (s == null || s.equals("") || dict.size() == 0)
            return false;

        for (int i = 1; i < s.length() + 1; i++)
        {
            String prefix = s.substring(0, i);
            String suffix = s.substring(i);
            // either both prefix and suffix is in the dict
            // or suffix can be recursively broken down further
            if (dict.contains(prefix) && (dict.contains(suffix) || helper(suffix))
            {
                this.memo.put(s, true);
                return true;
            }
        }

        this.memo.put(s, false);
        return false;
    }
}

```

Python:

```python

from functools import lru_cache

class Solution:
    def concatenatedWords(self, words):
        @lru_cache(None)
        def helper(word):
            if not word or word in words:
                return True
            for i in range(1, len(word)+1):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in words and helper(suffix):
                    return True
            return False

        words = set(words)
        result = list()
        for word in words:
            for i in range(1, len(word)+1):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in words and helper(suffix):
                    result.append(word)
                    break

        return result
```
