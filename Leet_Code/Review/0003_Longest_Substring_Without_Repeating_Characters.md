[3] Longest Substring Without Repeating Characters
==================================================

Given a string, find the length of the **longest substring** without repeating
characters.

**Example 1**:

```
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

Solution
--------

We may solve the problem in O(n) time complexity by simply iterate and build
the longest substring. As we build our substring, we check whether the new
character encountered is a repeat. If it is, then we know that current substring
is a candidate for longest substring. If not, then we simply append and build
up the substring.

**Python**:

```python
class Solution:
    def longest_substring_without_repeats(self, s):
        curr_substr = []
        longest_thus_far = 0
        for char in s:
            if char not in curr_substr:
                curr_substr += [char]
            else:
                curr_substr = curr_substr[curr_substr.index(char)+1:] + [char]
            longest_thus_far = max(longest_thus_far, len(curr_substr))
        return longest_thus_far
```



**Go**:

```go
func lengthOfLongestSubstring(s string) int {
    m := make(map[byte]int)
    result := 0
    lo, hi := 0, 0

    for hi < len(s) {
        char := s[hi]
        if count, ok := m[char]; !ok || (ok && count == 0) {
            m[char] = 1
            if hi - lo + 1 > result {
                result = hi - lo + 1
            }
            hi++
            continue
        }
        char := s[lo]
        lo++
        if count, ok := m[lo]; ok {
            m[lo] = count - 1
        }
    }
    return result
}
```

---

LeetCode:
[Longest-Substring-Without-Repeating-Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
