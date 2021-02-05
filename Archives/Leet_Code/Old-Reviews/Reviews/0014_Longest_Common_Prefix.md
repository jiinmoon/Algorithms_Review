14 Longest Common Prefix
========================

Question:
---------

Write a function to find the longest common prefix amongst an array of strings.

If there is no common prefix, return an empty string "".

Solutions:
----------

Naive approach would be to iterate over all strings from the beginning, and
check how far the prefix can extend. This will take O(n * m) where m is the
length of the shortest string and n is the number of strings to iterate.

The better approach would be to first sort the strings - this finds the two
strings which are shortest/longest and most different.

Codes:
------

Go:

```go
import "sort"

func longestCommonPrefix(str []string) string {
    if len(strs) == 0 {
        return ""
    } elif len(strs) == 1 {
        return strs[0]
    }
    sort.Strings(strs)
    var (
        s1 = strs[0]
        s2 = strs[len(strs)-1]
        i = 0
    )
    for ; i < len(s1) && s1[i] == s2[i]; i++ {}
    return s1[:i]
```

---

**Source:**

LeetCode:
[Longest-Common-Prefix](https://leetcode.com/problems/longest-common-prefix/)
