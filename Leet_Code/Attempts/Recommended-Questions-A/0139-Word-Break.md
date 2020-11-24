# 139. Word Break

Given a non-empty string s and a dictionary wordDict containing a list of
non-empty words, determine if s can be segmented into a space-separated
sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the
segmentation.
You may assume the dictionary does not contain duplicate words.

---

To determine whether the given string s can be broken down as a list of words
containing in the given wordDict, we may use dynamic programming to identify.
Whether a given substring is thus far fit the criteria is determined by the dp
array upto that index j where s[j:i] is the current substring considered.

---

Java:

```java

class Solution {

    public boolean wordBreak(String s, List<String> wordDict) {
        HashSet<String> words = new HashSet<>(wordDict);
        int m = s.length();
        boolean[] dp = new boolean[m+1];
        dp[0] = true;

        for (int i = 1; i < m + 1; i++) {
            for (int j = i - 1; i >= 0; j--) {
                if (dp[j] && words.contains(s.substring(j, i))) {
                    dp[i] = true;
                    break;
                }
            }
        }

        return dp[m];
    }
}

```

Python:

```python

class Solution:
    def wordBreak(self, s, words):
        words = set(words)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i - 1, -1, -1):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
        return dp[-1]
```
