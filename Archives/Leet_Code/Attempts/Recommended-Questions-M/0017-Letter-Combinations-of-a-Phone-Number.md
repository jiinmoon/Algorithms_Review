# 17 Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter
combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given
below. Note that 1 does not map to any letters.

---

We can approach this problem with how we would create a permutations from
a given list of candidates - but here, for each digit will be mapped to
a several letters. We use dfs which can complete the algorithm in O(v + e) time
complexity.

---

Java:

```java

class Solution {
    private char[][] map = new char[][] {
        {}, {},                 // 0, 1
        {'a', 'b', 'c'},        // 2
        {'d', 'e', 'f'},        // 3
        {'g', 'h', 'i'},        // 4
        {'j', 'k', 'l'},        // 5
        {'m', 'n', 'o'},        // 6
        {'p', 'q', 'r', 's'},   // 7
        {'t', 'u', 'v'},        // 8
        {'w', 'x', 'y', 'z'}    // 9
    };
    
    private String s;
    
    public List<String> letterCombinations(String digits) {
        if (digits == null || digits.equals(""))
            return new ArrayList<>();
        
        this.s = digits;
        List<String> result = new ArrayList<>();
        
        helper(0, new StringBuilder(), result);
        
        return result;
    }
    
    private void helper(int i, StringBuilder path, List<String> result)
    {
        if (i >= this.s.length()) {
            result.add(path.toString());
            return;
        }
        
        int curr = (int) this.s.charAt(i) - '0';
        for (char digit : this.map[curr])
        {
            path.append(digit);
            helper(i+1, path, result);
            path.deleteCharAt(path.length() - 1);
        }
    }
}

```

Python:

```python

class Solution:
    def letterCombinations(self, digits):
        dMap = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        def helper(candidates, path):
            if not candidates:
                result.append(path)
                return
            for letter in dMap[candidates[0]]:
                helper(candidates[1:], path + letter)
        
        result = list()
        helper(digits, "")

        return result
```
