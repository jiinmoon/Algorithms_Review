# Longest Substring Without Repeat

    Given a string, find the length of the longest substring without repeating
    characters.

    Example:

    The longest substring without repeating letters for "abcabcbb" is "abc", which
    the length is 3.

    For "bbbbb" the longest substring is "b", with the length of 1.

---

## Approach:

Use hashmap to record each of the characters position as we discover them. When
we encounter them again, we update our start pointer to where the character has
been last seen to update our substring upto the start of repeat character.

O(n) in both time and space complexity.

---

Python:

```python

class Solution:

    def solve(self, A):

        d = defaultdict(int)
        start, result = 0, 0

        for end, char in enumerate(A):
            
            if char in d:
                start = max(start, d[char])

            d[char] = end + 1
            result = max(result, end - start + 1)

        return result
```
