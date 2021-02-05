# 3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating
characters.

---

We may use the hashmap to record each of the character positions that we have
found thus far. Then, our starting positions of the substring automatically
increases as repeating characters will be overriden as we record the current
character indicies. This would be O(n) in time complexity and O(1) in space
complexity as there are only limited set of ascii characters to consider.

---

Java:

```java

class Solution3 {

    public int lengthOfLongestSubstring(String s)
    {
        // 127 is accepted smallest possible ascii character set
        int[] record = new int[127];
        int start = 0, longest = 0;
        // working with char array appears to be faster than String object
        char[] chars = s.toCharArray();

        for (int end = 0; end < chars.length; end++)
        {
            start = Math.max(start, record[chars[end]]);
            record[chars[end]] = end + 1;
            longest = Math.max(longest, end - start + 1);
        }

        return longest;
    }
}

```
