# 242. Valid Anagram

Given two strings s and t , write a function to determine if t is an anagram of
s.

---

#### (1) Sort.

By sorting the two strings lexicographically, we can check in O(n * log(n))
time by checking for equality. O(n) space is required for storing sorted
strings.

#### (2) Count characters.

We count the shorter characters and likewise, count the longer characters; If
these two does not match up, they are not anagrams. This is O(n) in time
complexity and space complexity.

---

Java: Count characters.

```java

class Solution242 {

    public boolean isAnagram(String s, String t) {
        
        int[] counter = new int[26];
        
        if (s.length() > t.length())
        {
            String temp = s;
            s = t;
            t = temp;
        }
        
        for (char c : s.toCharArray())
            counter[c - 'a']++;
        
        for (char c : t.toCharArray())
            if (--counter[c - 'a'] < 0)
                return false;
        
        return true;
    }
}
```
