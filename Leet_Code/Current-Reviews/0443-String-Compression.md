# 443. String Compression

Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating
characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead be
stored in the input character array chars. Note that group lengths that are 10
or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the
array.

 
 Follow up:
 Could you solve it using only O(1) extra space?

---

Use two pointers; curr each current character, we try to iterate forward until
we have characters that are same as current. We record the current character to
insertion point; and if there are more than 2 of same characters found, we also
record them as well.

O(n) in time complexity.

---

Python:

```python

class Solution443:

    def compress(self, chars):

        i, j, ins = 0, 0, 0

        while i < len(chars):

            # iterate until same character sequence
            while j < len(chars) and chars[i] == chars[j]:
                j += 1

            # record current character
            chars[ins] = chars[i]
            ins += 1

            # current sequence length greater than 1? record as well
            if j - i > 1:
                for digit in str(j - i):
                    chars[ins] = digit
                    ins += 1

            # move i upto j
            i = j

        return ins
```
