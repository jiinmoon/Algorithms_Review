# 29. Divide Two Integers

Given two integers dividend and divisor, divide two integers without using
multiplication, division, and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its
fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

---

The naive approach would be of course repeatedly subtract which would be O(n)
in time complexity. To improve the time complexity, we use bit manipulation.

Note that shifting to left indicates the multiplying by 2 and shifting to right
is the opposite effect.

So, we shift the given divisor as far left as possible until it is at least at
same or exceed the dividend. Then, reverse the process on the divisor, as we
subtract this value from the dividend. This would be O(log(n)) in time
complexity.

---

Python:

```python
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if not divisor:
            return None
        sign = (dividend < 0) ^ (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        
	# shift here is essentially amount of time we have doubled 2^shift
        shift = 1
        while dividend >= (divisor << 1):
            divisor <<= 1
            shift <<= 1
            
        result = 0
        while shift >= 1:
            # can still divide
            if dividend >= divisor:
                dividend -= divisor
                result += shift
            shift >>= 1
            divisor >>= 1
        
        if sign:
            result = -result
        return max(min(result, 2**31-1), -2**31)
```
