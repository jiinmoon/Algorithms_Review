# LeetCode Daily Challenge: August Week.2 - Day.3

## Question

Given a column title as appear in an Excel sheet, return its corresponding
column number.

Example:

```
"A" -> 1
"Z" -> 26
"AA" -> 27
```

## Solution

This is a simple base 26 conversion. Think as follows:

```
base26("A") = 1 * 26^0
base26("AA") = (1 * 26^1) + (1 * 26^0)
```

Go:

``go

func pow(base, i int) int {
    res := 1
    for i > 0 {
        res *= base
        i--
    }
    return res
}

func titleToNumber(s string) int {
    m := make(map[rune]int)
    for i, r := range "ABCDEFGHIJKLMNOPQRSTUVWXYZ" {
        m[r] = i+1
    }
    res := 0
    for i, r := range s {
        res += (m[r] * pow(26, len(s)-i-1))
    }
    return res
}
```

