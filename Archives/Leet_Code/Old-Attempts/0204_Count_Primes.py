""" 204. Count Primes

Question:

    Count the number of prime numbers less than a non-negative number, n.

+++

Solution:

    One possible solution is to actually generate the prime numbers upto n, then
    count the primes generated. One of such prime number generating algorithm
    would be Sieves of Eratosthenes.

"""

class Solution:
    def sievesOfEratosthenes(self, n):
        primes = [1] * n
        primes[0] = primes[1] = 0 # 0, 1 is not prime.
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                # if i is prime, then every multiples of i would be divisible by
                # i - which cannot be prime.
                primes[i*i:n:i] = [0] * len(primes[i*i:n:i])
        return primes

    def countPrimes(self, n):
        if n < 3:
            return 0
        return sum(sievesOfEratosthenes(n))
