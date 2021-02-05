# 829. Consecutive Numbers Sum

Given a positive integer N, how many ways can we write it as a sum of
consecutive positive integers?

---

We can represent N as a sum of consecutive integers then following holds:

```
For positive integer N, positive integer x upto k:

        N = (x + 1) + (x + 2) + ... + (x + k)

Here, we are iterating from 1 to k, thus we use summation formula to
consolidate further:

        N = (x * k) + (k * (k + 1)) / 2

```

Thus, we can isolate for unknown x. Time complexity would be O(n^0.5) as k is
growing - it is enough to examine value of k upto square root of N.

---

Java:

```java

class Solution {

    public int compute(int N, int k)
    {
        return N - (k * (k + 1)) / 2;
    }

    public int consecutiveNumbersSum(int N)
    {
        int k = 1, count = 0;
        int RHS = compute(N, k);

        while (RHS >= 0)
        {
            if (RHS % k++ == 0)
                count++;
            
            RHS = compute(N, k);
        }

        return count;
    }
}

```


