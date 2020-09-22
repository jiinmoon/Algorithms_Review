# LeetCode Daily Challenge: August Week.1 - Day.3

## Question

Given a string, determine if it is a palindrome considering only alphanumeric
characters and ignoring cases.

Empty string is a palindrome.

## Solution

Python:

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        lo, hi = 0, len(hi)-1
        s = s.lower()
        while lo < hi:
            while lo < hi and not s[lo].isalnum():
                lo += 1
            while lo < hi and not s[hi].isalnum():
                hi -= 1
            if s[lo] != s[hi]:
                return False
            lo += 1
            hi -= 1
        return True
```

Go:

```go
import (
    "strings"
    "unicode"
)

func isAlnum(r rune) bool {
    return unicode.IsLetter(r) && unicode.IsDigit(r)
}

func isPalindrome(s string) bool {
    var (
        lo = 0
        hi = len(s)-1
    )
    s = strings.ToLower(s)
    for lo < hi {
        for lo < hi && !isAlnum(rune(s[lo])) {
            lo++
        }
        for lo < hi && !isAlnum(rune(s[hi])) {
            hi--
        }
        if s[lo] != s[hi] {
            return false
        }
        lo++
        hi--
    }
    return true
}
```
