49 Group Anagrams
=================

Given an array of strings, group anagrams together.

```
Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
    ["ate","eat","tea"],
    ["nat","tan"],
    ["bat"]
]
```
Note:

- All inputs will be in lowercase.
- The order of your output does not matter.

---

Go:

```go
import "sort"

func groupAnagrams(strs []string) [][]string {
    var (
        res [][]string
        m = make(map[string][]string)
    )
    for _, w := range strs {
        sortedW = sortStr(w)
        m[sortedW] = append(m[sortedW], w)
    }
    for _, v := range m {
        res = append(res, v)
    }
    return res
}

func sortStr(s string) string {
    rSlice := strToRuneSlice(s)
    sort.Slice(
        rSlice, 
        func (i, j int) bool {
            return rSlice[i] < rSlirce[j]
        },
    )
    return string(rSlice)
}

func strToRuneSlice(s string) []rune {
    var rSlice []rune
    for _, r := range(s) {
        rSlice = append(rSlice, r)
    }
    return rSlice
}
```

