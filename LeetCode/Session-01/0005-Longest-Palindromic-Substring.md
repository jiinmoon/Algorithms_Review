# 5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

---

Naive approach would be to consider every possible substring lengths starting
from 2 and on to check for the palindrome. Since it is O(n^2) to generate all
possible substrings, and additional O(n) time to check for palinedrome on each
of the substrings, overall would be O(n^3) in time complexity.

Better method would be to consider every position on the string as the "centre"
point of our substring. Thus, as we iterate onwards, we expand to left and
right so long as it is a palindrome. Hence, we do not have to spend as much
time as naive approach since we can early exit on most cases where it is not
a palindrome. This would be O(n^2) in time complexity.

---

Python: Naive approach.

```python

# times out
class Solution5:

    def longestPalindrome(self, s):

        if not s or len(s) < 2:
            retun s

        longest = ""

        for i in range(len(s)):
            for j in range(i, len(s) + 1):
                if s[i:j] == s[i:j][::-1]:
                    longest = max(longest, s[i:j], key = len)

        return longest
```

Python: Centre approach.

```python

class Solution5:

    def longestPalindrome(self, s):
        
        if not s or len(s) < 2:
            return s

        longest = ""

        def expand(start, end):
            while start >= 0 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1
            return s[start+1:end]

        for i in range(len(s)):
            # odd and even cases
            s1 = expand(i, i)
            s2 = expand(i, i+1)
            longest = max([longest, s1, s2], key=len)

        return longest
```

Java: Centre approach.

```java

class Solution5
{
    private String expand(String s, int start, int end)
    {
        while (start >= 0 && end < s.length() && s.charAt(start).equals(s.charAt(end)))
        {
            start--;
            end++;
        }
        return s.substring(start+1, end);
    }

    public String longestPlaindrome(String s)
    {
        String longest, s1, s2;
        longest = "";

        for (int i = 0; i < s.length(); i++)
        {
            s1 = expand(s, i, i);
            s2 = expand(s, i, i+1);
            longest = Collections.max(
                Arrays.asList(longest, s1, s2),
                (String a, String b) ->
                    Integer.valueOf(a.length()).compareTo(b.length()));
        }
        return longest;
    }
}
```
