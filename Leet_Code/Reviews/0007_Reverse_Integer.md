7 Reverse Integer
=================

Question:
---------

Given a 32-bit signed integer, reverse digits of an integer.

Solutions:
----------

We could use binary opearations but I am not sure about actual speed
improvements. But the idea is that we repeatedly take the last digit of the
given num and append to the new result num. We need to also take care of signs
and overflow issues.

Codes:
------

Go:

```go
const MaxInt32 = 1<<31 - 1 // 2**31 - 1

func reverse(x int) int {
    var (
        result = 0
        sign = 1
    )
    if x < 0 {
        sign = -1
        x = x * -1
    }
    for x > 0 {
        result = (result * 10) + (x % 10)
        if result > MaxInt32 {
            return 0
        }
        x /= 10
    }
    return sign * result
}
```

---

**Source:**

LeetCode: [Reverse-Integer](https://leetcode.com/problems/reverse-integer/)
