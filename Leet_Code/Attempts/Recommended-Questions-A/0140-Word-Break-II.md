# 140. Word Break II

Given a non-empty string s and a dictionary wordDict containing a list of
non-empty words, add spaces in s to construct a sentence where each word is
a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the
segmentation.
You may assume the dictionary does not contain duplicate words.

---

Firstable, we should check whether the given string can be broken down into the
words that should be found within the wordDict. This can be done with dynammic
programming checking for whether the substring upto j can be broken down or
not. This first process would be of O(n) in time complexity (same algorithm as
the question #139).

Then for the second part we should actually break down the string into as many
possbile different ways. To do so, we use recursion and memoization: for each
starting point, we create a prefix and suffix is generate recursively while
checking for their membership within the wordDict.

---

Java:

```java

import java.util.HashMap;

class Solution {

    public List<String> wordBreak(String s, List<String> wordDict) {
        return helper(s, wordDict, 0, new HashMap<>());
    }

    public List<String> helper(String s, List<String> wordDict, int left, Map<Integer, List<String>> memo) {
        // every index has fixed solution - use memoization to avoid duplicate
        if (memo.containsKey(left))
            return memo.get(left);

        // from every position, consider every word
        List<string> result = new LinkedList<>();
        for (String word : wordDict) {
            if (s.startsWith(word, left)) {
                // prefix
                if (s.length() == word.length() + left) {
                    result.add(word);
                // there are more suffixes to discover
                } else {
                    List<String> suffixes = helper(s, wordDict, left + word.length(), memo);
                    // concatenate all suffixes to prefix
                    for (String suffix : suffixes)
                        result.add(word + " " + suffix);
                }
            }
        }

        memo.put(left, result);

        return result;
    }
}


```

Python:

```python

class Solution:
    def wordBreak(self, s, words):
        words = set(words)
        if not self.isBreakable(s, words):
            return []
        result = self.breakStr(0, {}, s, words)
        return ["".join(r) for r in result]

    def isBreakable(self, s, words):
        m = len(s)
        dp = [False] * (m + 1)
        dp[0] = True
        for i in range(1, m + 1):
            for j in range(i - 1, -1, -1):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
        return dp[-1]

    def breakStr(self, left, memo, s, words):
        if left >= len(s):
            return [[]]
        if left in memo:
            return memo[left]

        result = list()
        for i in range(left + 1, len(s) + 1):
            prefix = s[:i]
            suffixes = self.breakStr(i, memo, s, words)
            if prefix in words and suffixes:
                for suffix in suffixes:
                    result.append([prefix] + suffix)
        memo[left] = result
        return result
```
