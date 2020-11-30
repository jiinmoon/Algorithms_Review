# 1328. Break a Palindrome

Given a palindromic string palindrome, replace exactly one character by any
lowercase English letter so that the string becomes the lexicographically
smallest possible string that isn't a palindrome.

After doing so, return the final string.  If there is no way to do so, return
the empty string.

---

Here, we may use two pointers method to find the first character that is not
a palindrome. However, we should note that if that character found is
a palindrome and lowest possible string ('a'), then we should move forward as
we cannot change to greater lexicographical string.

Once we do so, we have two cases: string is lowest possible form that is
palindrome or first point where not 'a' is found. If the palindrome is already
in lowest form, then all we can do is change the last character of the
palindrome (i.e. 'aaaa' to 'aaab'). Otherwise, we can change the whichever
first character found that is not 'a' to 'a'.

Time complexity would be O(m).

---

Java:

```java

class Solution {

    public String breakPalindrome(String palindrome)
    {
        // base case
        if (palindrome.length() < 2)
            return "";

        char[] chars = palindrome.toCharArray();
        int l = 0, r = chars.length - 1;

        while (l < r && chars[l] == chars[r] && chars[l] == 'a') { l++; r--; }

        if (l >= r) chars[chars.length-1] = 'b';
        else chars[l] = 'a';

        return new String(chars);
    }

}

```
