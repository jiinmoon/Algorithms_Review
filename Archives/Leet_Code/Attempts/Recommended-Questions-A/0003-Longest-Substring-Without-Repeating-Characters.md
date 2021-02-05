# 3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating
characters.

---

Consider building our substring as we iterate on forward. For each character
that we encounter, we check to see whether duplicate entry has been found in
our current substiring. If so, then our current substring window is fixed to
previous occurrence of the duplicate character. Here, it is possible that
duplicate entry can be found before the previous start position - hence, we
need to take the maximum value between two while updating our window.

Time complexity would be O(n) as well as space required to store information
about our substring.

---

Java:

```java

class Solution {

    public int longestSubstringWithoutRepeats(String s)
    {
        if (s == null || s.equals("")) return 0;
        if (s.length() < 2) return 1;

        int longestThusFar = 0, start = 0;
        // maps character to its previously seen index
        HashMap<Character, Integer> m = new HashMap<>();

        for (int i = 0; i < s.length(); i++)
        {
            char newChar = s.charAt(i);
            if (m.containsKey(newChar))
                // duplicate has been found; update substring start to previous + 1
                start = Math.max(start, m.get(newChar) + 1);

            longestThusFar = Math.max(longestThusFar, i - start + 1);
            m.put(newChar, i);
        }

        return longestThusFar;
    }
}

```
