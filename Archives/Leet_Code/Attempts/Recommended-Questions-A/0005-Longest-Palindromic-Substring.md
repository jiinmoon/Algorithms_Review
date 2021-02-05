# 5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

---

Instead of performing exhaustive search of considering every substring of every
length, we treat each of the character as a mid point in the substring and
expand out as far out as possible to check for the palindrome.

---

```java

class Solution {
    public String longestPalindrome(String s) {
        String longest = "";
        for (int i = 0; i < s.length(); i++) {
            String s1 = expand(s, i, i);
            String s2 = expand(s, i, i+1);
            longest = Collections.max(
                Arrays.asList(longest, s1, s2),
                (String a, String b) -> {
                    return Integer.valueOf(a.length()).compareTo(b.length());
                });
        }
        return longest;
    }

    private String expand(String s, int start, int end) {
        while (start >= 0 && end < s.length() and s.charAt(start) == s.charAt(end)) {
            start--;
            end++;
        }
        return s.substring(start+1, end);
    }
}
```

Python:

```python

class Solution:
    def longestPalindromicSubstring(self, s):
        longest = ""
        for i in range(len(s)):
            s1 = self.expand(s, i, i)
            s2 = self.expand(s, i, i+1)
            longest = ([longest, s1, s2], key=len)
        return longest

    def expand(self, s, start, end):
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
        return s[start+1:end]
```
