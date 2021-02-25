# 3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating
characters.

---

We can find the length of the longest substring without repeating characters in
a single pass by recording each of the characters and their index of where we
have seen them last. To do so, we use hashmap to efficiently store, update, and
retrieve the information of character to index pairing. This would be O(n) in
both time complexity and space complexity. More rigorously, space complexity
would actually be constant as there are only limited number of characters that
we need to record their last seen positions.

---

Python:

```python

class Solution3:

    def lengthOfLongestSubstring(self, s):

        d = dict()
        start, longest = 0, 0

        for end, char in enumerate(s):
            # char has been seen previously? 
            # update the start of current substring
            start = max(start, d.get(char, 0))

            # record the current new end point
            # update potentially new substr with greater length
            d[char] = end + 1
            longest = max(longest, end - start + 1)

        return longest
```

Java:

```java

class Solution3
{
    public int lengthOfLongestSubstring(String s)
    {
        // assume unicode encoding; 128 space is enough
        int[] record = new int[127];
        int start, longest;
        start = longest = 0;

        // convert to char array; more efficient then working with String object
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
