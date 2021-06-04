# 7. Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. If
reversing x causes the value to go outside the signed 32-bit integer range
[-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or
unsigned).

---

We iterate on every digit of the given integer x, extract the current digit to
build our reversed integer result. x can be negative hence we should record the
sign of the given integer as well as check whether the integer overflows. The
time complexity is constant as we only have to iterate on 32 bits.

---

Python:

```python

class Solution7:

    def reverseInteger(self, x):

        sign = (x > 0) - (x < 0)
        x = abs(x)
        result = 0

        while x:
            x, curr = divmod(x, 10)
            result = result * 10 + curr

            if result >= 2**31 - 1 or sign * result <= -2**31:
                return 0

        return sign * result
```

