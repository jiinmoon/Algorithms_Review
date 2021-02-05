# 1416. Restore The Array

A program was supposed to print an array of integers. The program forgot to
print whitespaces and the array is printed as a string of digits and all we
know is that all integers in the array were in the range [1, k] and there are
no leading zeros in the array.

Given the string s and the integer k. There can be multiple ways to restore the
array.

Return the number of possible array that can be printed as a string s using the
mentioned program.

The number of ways could be very large so return it modulo 10^9 + 7

---

We can use dynammic programming to find all different ways that we can restore
the array.

Let us prepare a dp array where dp at i will represent total number of ways
that we can restore upto that i-th point. Then, at each i, we look behind as
much as possible and examine the substring from j starting at i - 1 to 0.

Then, at each i, we have substring between s[j:i]. Now, s[j:i] falls under
following cases to update our dp[i]:

(1) length of substring is greater than what is possible; we know that length
has to be bounded by k.

(2) s[j] is '0'; we ignore the leading zero cases (i.e. '0123...').

(3) int represented by the substring is greater than k, which indicates it is
invalid.

(4) otherwise, we can update at dp[i] for previous substring upto dp[j].

---

Python:

```python

class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
    
        dp = [0] * (len(s) + 1)
        
        # bound is needed for early exit
        # time limit exceeded without it
        bound = len(str(k))
        for i in range(1, len(s)+1):
            for j in range(i-1,-1,-1):
                if i-j > bound or int(s[j:i]) > k:
                    break
                if s[j]=='0':
                    continue
                dp[i] += dp[j] if j > 0 else 1
                dp[i] %= 10 ** 9 + 7
        return dp[-1]

```
