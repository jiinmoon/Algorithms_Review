# 266. Palindrome Permutation

Given a string, determine if a permutation of the string could form
a palindrome.

---

To determine whether a given string and its character combinations can form
a palindrome or not, we may only need to check how many odd and even number of
each characters are present. The even characters can be paired to each other
for a valid palindrome. In the case of odd character, there has to be at most
1 odd character which occupies the mid in order to form a valid paldinrome
permutation of the string. The time complexity of this approach would be O(n).

---

Python:

```python

class Solution:
    def canPermutePalindrome(self, s):
        counter = collections.Counter(s)
        result = [c % 2 for c in counter.values()]

        return sum(result) <= 1
```
