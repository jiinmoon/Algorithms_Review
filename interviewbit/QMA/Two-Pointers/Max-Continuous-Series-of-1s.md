# Max Continuous Series of 1s

You are given with an array of 1s and 0s. And you are given with an integer M,
which signifies number of flips allowed.

Find the position of zeros which when flipped will produce maximum continuous
series of 1s.

For this problem, return the indices of maximum continuous series of 1s in
order.

---

Use two pointers to denote the beginning and end of our current continuous
subarray of ones. For each new value encountered, we check to see that it is
zero or not.

If new value is zero, we decrement our count of flips allowed. Then, until we
can restore the amount of flips, we move our start pointer forward while
updating flip count if start is found to be zero as well.

Amongst all the subarrays found, we find the maximum amongst them.

O(n) in time complexity.

---

Python:

```python

class Solution:

    def maxones(self, A, B):

        l, r, zeroes = 0, 0, 0
        i, j = 0, 0

        while j < len(B):

            if zeroes <= B:
                zeroes += nums[j] == 0
                j += 1

            if zeroes > B:
                zeroes -= nums[i] == 0
                i += 1

            if r - l < j - i:
                r, l = j, i

        return [i for i in range(l, r)]
```
