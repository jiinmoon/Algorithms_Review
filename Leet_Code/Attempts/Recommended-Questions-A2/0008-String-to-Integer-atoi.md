# 8. String to Integer (atoi)

Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until
the first non-whitespace character is found. Then, starting from this character
takes an optional initial plus or minus sign followed by as many numerical
digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral
number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid
integral number, or if no such sequence exists because either str is empty or
it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered a whitespace character.
Assume we are dealing with an environment that could only store integers within
the 32-bit signed integer range: [−23^1,  23^1 − 1]. If the numerical value is
out of the range of representable values, 23^1 − 1 or −23^1 is returned.

---

First, we should sanitize the given string to remove as much whitespaces as
possible. Then, we need to remember that number can be negative - if '-' sign
is present we should also make a note of it.

Once we have our clean string, we can now iterate as far as possible while
checking for each character is a digit or not - if it is, we add to our result
while shifting our result to left by 10.

Time complextiy would be of O(n).

---

Java:

```java

class Solution8 {

    public int atoi(String s)
    {
        if (s == null || s.length() < 1)
            return 0;

        char[] chars = s.toCharArray();

        int i = 0;
        while (i < chars.length - 1 && chars[i] == ' ')
            i++;

        boolean isNeg = chars[i] == '-';
        i = (isNeg || chars[i] == '+') i + 1 : i;

        long result = 0;

        for (;i < chars.length; i++)
        {
            if (Character.isDigit(chars[i])) {
                result = result * 10 + chars[i] - '0';
                if (result > Integer.MAX_VALUE || result * -1 < Integer.MIN_VALUE)
                    return (isNeg) ? Integer.MIN_VALUE : Integer.MAX_VALUE;
            } else {
                break;
            }
        }

        return (isNeg) ? (int) result * -1 : (int) result;
    }
}

```

Python:

```python

class Solution8:

    def atoi(self, s):

        s = s.strip()

        if not s:
            return 0

        isNeg = s[0] == '-'
        s = s[1:] if isNeg else s

        result = 0

        for i, char in enumerate(s):
            if char.isdigit():
                result = result * 10 + int(char)
            else:
                break

        result = result * -1 if isNeg else result

        return max(min(result, -2**31), 2**31-1)
```
