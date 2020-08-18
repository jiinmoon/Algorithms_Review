763 Partition Labels
====================

A string s of lowercase English letters is given. We want to partition this
string into as many parts as possible so that each letter appears in at most
one part, and return a list of integers representing the size of theseparts.

---

We will create a record of all the characters and their last appearences in the
given string; when we iterate on the S, we can check whether the current
character has reached the end of its last appearences so that we can save the
current segment and move onto new.

---

Go:

```go
func partitionLabels(S string) []int
{
    var (
        record = make(map[rune]int)
        res = []int{}
        srt, end = 0, 0
    )
    for i, r := range S { record[r] = i }
    for i, r := range S {
        end = max(end, record[r])
        if i == end {
            res = append(res, end - srt + 1)
            srt = i + 1
        }
    }
    return res
}

func max(x, y int) int
{
    if (x >= y) { return x }
    return y
}
```
