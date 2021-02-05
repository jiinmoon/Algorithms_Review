# 2. Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Note:

Assume we are dealing with an environment that could only store integers within
the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this
problem, assume that your function returns 0 when the reversed integer
overflows.

---

Going through digit after digit with modulo operation and build our reversed
integer. Since we have a limited number of digits in a given integer range the
time complexity is O(log(x)).

---

Python:

```python

class Solution2:

    def reverse(self, x):

        sign = (x > 0) - (x < 0)

        result = 0
        while x:
            x, digit = divmod(x, 10)
            result = result * 10 + digit

        result *= sign

        if result < -2**31 or result > 2**31 - 1:
            return 0
        return result

```
