139 Word Break
==============

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:

```
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
```

Example 2:

```
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
```

Example 3:

```
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
```

---

We may use dynamic programming technique here to check all the prefixes upto
length of the s. The current value in the dp array would be true if the
previous prefix upto that point was true, and current word being considered is
in the given dictionary.

---

Go:

Dynamic programming approach.

```
func wordBreak(s string, wordDict []string) bool {
    m := len(s)
    dp := make([]bool, m+1)
    dp[0] = true
    wordMap := make(map[string]struct{})
    for _, word := range wordDict {
        wordMap[word] = struct{}{}
    }
    for i := 1; i < m+1; i++ {
        for j := i-1; j > -1; j-- {
            if _, ok := wordMap[s[j:i]]; dp[j] && ok {
                dp[i] = true
                break
            }
        }
    }
    return dp[m]
}
```
