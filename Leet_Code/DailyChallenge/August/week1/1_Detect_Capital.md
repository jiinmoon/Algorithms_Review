 # LeetCode Daily Challenge: August Week.1 - Day.1

 ## Question

 Given a word, you need to judge whether the usage of capitals in it is right
 or not.

 We define the usage of capitals in a word to be right when one of the
 following cases holds:

    All letters in this word are capitals, like "USA".
    All letters in this word are not capitals, like "leetcode".
    Only the first letter in this word is capital, like "Google".
 
 Otherwise, we define that this word doesn't use capitals in a right way.

## Solution

Python:

```python
class Solution:
    def detectCapitalUse(self, word):
        if not word:
            return
        capitalCount = sum([1 for char in word if char.isupper()])
        return (capitalCount == len(word) or \
                (not capitalCount) or \
                (word[0].isupper() and capitalCount == 1)
```

