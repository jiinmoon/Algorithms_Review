3 Longest Substring Without Repeating Characters
================================================

Question:
---------

Given a string, find the length of the **longest substring** without repeating
characters.

Solutions:
----------

To find the longest substring without repeating characters, we will iterate on
the given string while building the substring ourselves. If the duplicate
element is found, then we know that we have a canddiate for the longest
substring. We record the length, and update our substring such that substring
upto the previously repeating character is removed and new one is added.

Codes:
------

Go:

```go
import "strings"

func max (x, y int) int {
    if x >= y {
        return x
    }
    return y
}

func lengthOfLongestSubstring(s string) int {
    var (
        longestThusFar int
        substring string
    )
    for _, char := range s {
        if strings.ContainsRune(substring, char) {
            substring = substring[strings.IndexRune(substring, char)+1:]
        }
        substring += string(char)
        longestThusFar = max(longestTHusFar, len(substring)
    }
    return longestThusFar
```

---

**Source:**

LeetCode: [Longest-Substring-Without-Repeating-Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters)
