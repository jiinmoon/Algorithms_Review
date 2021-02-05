# 680. Valid Palindrome II

Given a non-empty string s, you may delete at most one character. Judge whether
you can make it a palindrome.

---

The simplest approach would be to iterate on the given string and try to
generate a string that has a single character removed to check for palindrome.
This is a O(n^2) in time complexity.

Better approach would be similar in that we still iterate on the given string
while checking for the first and last characters. If they are same, then we can
move on forward. If not, then this is where the discrepency occurs - hence, we
either remove the first and last and check for whether we can form the
palindrome. This would be O(n) in time complexity.

---

Java:

```java

class Solution {
    
    public boolean isValidPalindrome(String s) {
        int m = s.length();
        int i = 0;
        while (i < (m + 1) / 2) {
            if (s.charAt(i) != s.charAt(m - i - 1) {
                String f = s.substring(i+1, m - i);
                String b = s.substring(i, m - i - 1);
                String rev_f = new StringBuilder(f).reverse().toString();
                String rev_b = new StringBuilder(b).reverse().toString();
                return f.equals(rev_f) || b.equals(rev_b);
            }
            i++;
        }
        return true;
    }
}

```

Python:

```python

class Solution:
    def isValidPalindrome(self, s):
        m = len(s)
        i = 0
        while i < n // 2:
            # first and last not same?
            # try to remove first or last and check
            if s[i] != s[n - 1 - i]:
                front = s[i+1:n-i]
                back = s[i:n-1-i]
                return front == front[::-1] or back == back[::-1]
            i += 1
        return True
```
