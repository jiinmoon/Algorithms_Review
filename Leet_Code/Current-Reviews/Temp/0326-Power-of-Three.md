# 326. Power of Three

Given an integer n, return true if it is a power of three. Otherwise, return
false.

An integer n is a power of three, if there exists an integer x such that n ==
3x.

---

#### (1) Brute Force.

Repeatedly divide by 3 until no remainder is left. If n is 1 then it is power
of three. O(log(n)) in time complexity as we only repeat the division log base
3.
#### (2) Integer Limit.

Since we know the limi of the integer, there are only handful of power of
threes that can fit within that range. Thus, generating is constant time (or
truly hardcode all the values). O(1) in time complexity.

#### (3) Log Math.

Consider following:

```

n = 3 ^ x

# log both sides
log3(3) * x = log3(n)
x = log3(n)

# log base conversion to log base 10
x = log10(n) / log10(3)

```

Hence, we check for whether x is is an integer. Time complexity solely depends
upon efficiency of `log` function used.

---

Java: Integer Limit.

```java

class Solution {
    
    Set<Integer> solutions = new HashSet<>();
    
    public Solution()
    {
        for (int i = 1; 0 < i && i < Integer.MAX_VALUE; i *= 3)
            this.solutions.add(i);
    }
    
    public boolean isPowerOfThree(int n) {
        return this.solutions.contains(n);    
    }
}

```
