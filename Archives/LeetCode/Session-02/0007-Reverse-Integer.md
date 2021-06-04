# 7. Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. If
reversing x causes the value to go outside the signed 32-bit integer range
[-2^31, 2^31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or
unsigned).

---

To reverse a given integer, we can take the integer digit by digit while
reversing it. There are several edge cases that we should be aware of however.
First, the sign of the integer is important and should be recorded prior to
operations to follow. Second, as the environment assumes 64-bit sized integers,
we should also be careful to avoid overflow issues by constantly checking to
see whether the current value overflowed or not.

---

Python:

```python

class Solution7:

    def reverseInteger(self, num):

        sign = (x > 0) - (x < 0)

        num = abs(num)
        
        result = 0

        while num:
            num, curr = divmod(num, 10)
            result = result * 10 + curr

            if result * sign >= 2**31 or result * sign < -2**31:
                return 0

        return sign * result
```
