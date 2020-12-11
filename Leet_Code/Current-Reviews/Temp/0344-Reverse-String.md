# 344. Reverse String

Write a function that reverses a string. The input string is given as an array
of characters char[].

Do not allocate extra space for another array, you must do this by modifying
the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

---

Java:

```java

class Solution344 {

    public void reverseString(char[] s)
    {
        for (int l = 0, r = s.length-1; l < r; l++, r--)
        {
            char temp = s[l];
            s[l] = s[r];
            s[r] = temp;
        }
    }
}

```
