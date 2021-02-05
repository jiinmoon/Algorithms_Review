# 387. Frist Unique Character in a String

Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

---

Count occurrences of each character; iterate forward checking its count and return its index if count is 1.

O(n) in both time and space complexity.

---

Java:

```java
class Solution387 {

    public int firstUniqChar(String s) {

        int[] seen = new int[26];
        char[] chars = s.toCharArray();
        
        for (char c : chars)
            seen[c - 'a']++;
        
        for (int i = 0; i < chars.length; i++)
            if (seen[chars[i] - 'a'] == 1)
                return i;
        return -1;
    }
}
```
