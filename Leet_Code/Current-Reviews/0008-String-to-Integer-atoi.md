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
the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is
out of the range of representable values, 231 − 1 or −231 is returned.

---

First, we sanitize the given input string by removing all the whitespace
character in front. Then, we check for any sign "+-" and record whether we
should negate the final result.

Then, we iterate on the string so long as the character can be interpreted as
a digit and build our result. Here, we should check that result does not
overflor nor underflow.

This would be O(n) in time complexity and O(1) in space as space is bounded by
the size of integer.

---

Java:

```java

class Solution8 {

    public int myAtoi(String s)
    {
        if (s == null || s.length() < 1)
            return 0;
        
        char[] chars = s.toCharArray();
        int i = -1;

        while (i++ < chars.length && chars[i] == ' ');

        if (i == chars.length)
            return 0;

        boolean isNeg = chars[i] == '-';
        i = (isNeg || chars[i] == '+') i + 1 : i;
        
        int result = 0;

        while (i++ < chars.length)
        {
            if (!Character.isDigit(chars[i-1]))
                break;

            result = result * 10 + chars[i-1] - '0';

            if (result > Integer.MAX_VALUE || result * -1 < Integer.MIN_VALUE)
                return (isNeg) ? Integer.MIN_VALUE : Integer.MAX_VALUE;
        }
        
        return (isNeg) ? result * -1 : result;
    }
}

```
