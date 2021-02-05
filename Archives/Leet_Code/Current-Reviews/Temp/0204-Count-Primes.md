# 204. Count Primes

Count the number of prime numbers less than a non-negative number, n.

---

We can use Sieves of Eratosthenes - starting for each value from 2, we find
every value squared and mark it as non-prime. Its precise time complexity is
O(n * log (log (n))) since for every num upto n, as primes are discovered, we
do not have to itearte again to mark them as nonprimes.

---

Python:

```python

class Solution204:

    def countPrimes(self, n):

        primes = [True] * n

        for i in range(2, int(math.sqrt(n)) + 1):
            if primes[i]:
                primes[i*i:n:i] = [False] * len(primes[i*i:n:i])
        
        # remember to skip over first two non-primes 0 and 1.
        return sum(isPrime for isPrime in primes[2:] if isPrime)

```
