# Colorful Number

    For Given Number N find if its COLORFUL number or not

    Return 0/1

    COLORFUL number:

    A number can be broken into different contiguous sub-subsequence parts. 
    Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245. 
    And this number is a COLORFUL number, since product of every digit of
    a contiguous subsequence is different

---

## Approach:

Generate all subsequences and compute the product. If we have repeated product,
then N is not a colorful number. Use set or hashmap for O(1) look up. Due to
having to generate all subsequences, O(n^2) in time complexity.

---

Python:

```python

class Solution:

    def colorfulNumber(self, A):

        arr = []
        while A:
            A, x = divmod(A, 10)
            arr.append(x)

        seen = set()
        for i in range(len(arr)):
            temp = 1
            for j in range(i, len(arr)):
                temp *= arr[j]
                if temp in seen:
                    return 0
                seen.add(temp)
        
        return 1
```
