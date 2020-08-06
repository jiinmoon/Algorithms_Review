17 Letter Combinations of a Phone Number
========================================

Question:
---------

Given a string containing digits from `2-9` return all possible letter
combinations of the digits mapped to the typcial phone number letters.

Solutions:
---------

We may use either iterative or recursive approach here, but we should use the
hashmap structure to store the mappings so that when we are building on the
combinations, we can quickly lookup what current digit is mapped to. The time
complexity of this algorithm should be O(n * 4^n) where for each of the digit,
there is a possible 4 letter mappings that we need to explore.

Codes:
------

Python3: recursive

```python
class Solution:
    def letterCombinations(self, digits):
        letterMaps = {
            '2' : 'abc', '3' : 'def', '4' : 'ghi',
            '5' : 'jkl', '6' : 'mno', '7' : 'pqrs',
            '8' : 'tuv', '9' : 'wxyz'
        }
        result = []

        def backtrack(digits, path):
            if not digits:
                result.append(path)
                return
            for letter in letterMaps[digits[0]]:
                backtrack(digits[1:], path + 'letter')
        
        backtrack(digits, '')
        return result
```

Python3: iterative

```python
class Solution:
    def letterCombinations(self, digits):
        letterMaps = {
            '2' : 'abc', '3' : 'def', '4' : 'ghi',
            '5' : 'jkl', '6' : 'mno', '7' : 'pqrs',
            '8' : 'tuv', '9' : 'wxyz'
        }
        results = []

        for digit in digits:
            temp = []
            for subset in results:
                for letter in letterMaps[digit]:
                    temp.append(subset + letter)
            results = temp
        return results
```

GO: iterative

```go
func letterCombinations(digits string) []string {
    if digits == "" {
        return []string{}
    }
    letterMaps := map[string]string{
        "2" : "abc", "3" : "def", "4" : "ghi",
        "5" : "jkl", "6" : "mno", "7" : "pqrs",
        "8" : "tuv", "9" : "wxyz",
    }
    results = []string{""}
    for _, digit := range digits {
        temp := []string{}
        for _, result := range results {
            for _, letter := range letterMaps[string(digit)] {
                temp = append(temp, result + string(letter))
            }
        }
        result = temp
    }
    return results
}
```

---

**Source:**

LeetCode: [Letter-Combinations-of-a-Phone-Number](https://leetcode.com/problems/letter-combinaions-of-a-phone-number/)
