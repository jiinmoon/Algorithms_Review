227 Basic Calculator II
=======================

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators
and empty spaces . The integer division should truncate toward zero.


Example 1:

```
Input: "3+2*2"
Output: 7
```

Example 2:

```
Input: " 3/2 "
Output: 1
```

Example 3:

```
Input: " 3+5 / 2 "
Output: 5
```

---

We can utilize stack to build a list of numbers to add up together in the end.
THe problem here is dealing with the operator precedence, it is resolved if we
do not compute the numbers first, but defer the sum to later. Thus, we can pop
from the previous value from the stack and perform operation with * and /.

---

Go:

```go
import "unicode"

func calculate(s []string) int {
    var (
        stk = []int{}
        op = '+'
        num = 0
        res = 0
    }
    s += "+"
    for _, r := range s {
        if unicode.IsDigit(r) {
            num = (num * 10) + int(r - '0')
        } else if r == ' ' {
            continue
        } else {
            switch op {
            case '+':
                stk = append(stk, num)
            case '-':
                stk = append(stk, -num)
            case '*':
                lst := stk[len(stk)-1]
                stk = stk[:len(stk)-1]
                stk = append(stk, lst * num)
            case '/':
                lst := stk[len(stk)-1]
                stk = stk[:len(stk)-1]
                stk = append(stk, lst / num)
            }
            num = 0
            op = r
    for _, num := range stk {
        res += num
    }
    return res
}
