8 String to Integer (atoi)
==========================

Question:
---------

Implement `atoi` which converts a string to an integer.

Solutions:
----------

It varies for each langauge as to how encoding is handled, but the basic idea
is that the integer in string is still formatted in binary format as a data.
And since 0-9 is placed next to each other, their relative distance can be
found.

Codes:
------

Go:

```go
import "strings"

const (
    MaxInt32 = 1 << 31 - 1
    MinInt32 = -1 << 31 - 1
)

func myAtoi(str string) int {
    var (
        result = 0
        sign = 1
    )
    str = strings.TrimLeft(str, " ")
    for i, r := range str {
        if i == 0 && r == '-' {
            sign = - 1
            continue
        } else if i == 0 && r == '+' {
            continue
        } else if r < '0' || r > '9' {
            break
        }
        result = (result * 10) + int(r - '0')
        if sign * result <= MinInt32 {
            return MinInt32
        } elseif result >= MaxInt32 {
            return maxInt32
        }
    }
    return sign * result
}
```

---

**Source:**

LeetCode: [String-to-Integer-atoi](https://leetcode.com/problems/string-to-integer-atoi/)
