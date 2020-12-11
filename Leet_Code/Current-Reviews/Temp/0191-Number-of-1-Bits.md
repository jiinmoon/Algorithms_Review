# 191. Number of 1 Bits

Write a function that takes an unsigned integer and returns the number of '1'
bits it has (also known as the Hamming weight).

---

#### (1). Bit shift and check each digit.

Shift the n by 1 to right each time and count each digit extracted. O(log(n))
due to having to explore digits on n.

#### (2). Bit operation.

Another trick involving bit is removing counted digits 1s by using bit
operation &.

```
n           = 1011
n - 1       = 1010

n & n - 1   = 1010      reduces counted digit at last place

```

Time comlexity is same; one could argue for constant since number of digits is
limited in unsigned integer (typically under 32 digits).

---

Java:

```java

public class Solution {

    // you need to treat n as an unsigned value
    public int hammingWeight(int n) 
    {
        int count = 0;
        for (; n != 0; n &= (n - 1), count++);
        return count;
    }
}

```
