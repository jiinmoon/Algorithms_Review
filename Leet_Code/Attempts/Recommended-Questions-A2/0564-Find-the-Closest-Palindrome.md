# 564. Find the Closest Palindrome

Given an integer n, find the closest integer (not including itself), which is
a palindrome.

The 'closest' is defined as absolute difference minimized between two integers.

---

Let's visualize with an example. Suppose we are given integer 1234567.

Then, we see that to make this into a palindrome, we have to find the mid way
point and mirror one half into another. For example, we can see that closest
palindrome has to be 1234321.

Suppose that the given integer is a palindrome itself such as 1234321. Then,
only possible way to reduce it into another palindrome that is smaller has to
happen at the mid-way point; which is at 4. The answer would be 1233321.

So, the plan would be first identify the mid-way point where change has to
occur. There are three choices - we do not have to make any changes, or
increment or decrement the value found at mid-way point. Then, try to create
a palindrome for theses cases and return whichever that is smallest in their
difference with the given integer.

---

Python:

```python

class Solution564:

    def nearestPalindromic(self, n: str) -> str:
        
        def helper(val):
            temp = list(str(val))
            i, j = 0, len(temp)-1
            while i < j:
                temp[j] = temp[i]
                i += 1
                j -= 1
            return int("".join(temp))
        
        mid = 10 ** (len(n) // 2)
        n = int(n)
        original = helper(n)
        
        // find mid-way point where palindrome centre is
        // increment and decrement to check the difference
        // same as left shifting by mid-way point and copy left into right
        larger = helper((n // mid) * mid + mid + 1)
        smaller = helper((n // mid) * mid- 1)

        if original > result and original < larger:
            larger = original
        elif original < result and original > smaller :
            smaller = original
        
        return str(smaller) if result - smaller <= larger - result else str(larger)
```

