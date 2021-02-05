# Count and Say

The count-and-say sequence is the sequence of integers beginning as follows:

1, 11, 21, 1211, 111221, ...
1 is read off as one 1 or 11.
11 is read off as two 1s or 21.

21 is read off as one 2, then one 1 or 1211.

Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

---

We repeat generating count-and-say sequence n number of times, building upon
previous iterations.

For each step, we have two pointers; one moves forward while it is same as the
current character that is being examined here. We record its count and move on.

O(2^n) in time complexity as the sequence can double its size every step.

---

Python:

```python

class Solution:
    # @param A : integer
    # @return a strings
    def countAndSay(self, A):
        
        if A <= 0:
            return ""
        if A == 1:
            return "1"
        
        prev = "1"
        while A > 1:
            curr = ""
            i = 0
            while i < len(prev):
                j = i + 1
                while j < len(prev) and prev[i] == prev[j]:
                    j += 1
                curr += (str(j - i) + prev[i])
                i = j
            prev = curr
            A -= 1
        return prev
```
