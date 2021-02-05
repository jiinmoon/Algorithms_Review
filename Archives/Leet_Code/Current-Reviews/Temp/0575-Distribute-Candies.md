# 575. Distribute Candies

Alice has n candies, where the ith candy is of type candyType[i]. Alice noticed
that she started to gain weight, so she visited a doctor.

The doctor advised Alice to only eat n / 2 of the candies she has (n is always
even). Alice likes her candies very much, and she wants to eat the maximum
number of different types of candies while still following the doctor's advice.

Given the integer array candyType of length n, return the maximum number of
different types of candies she can eat if she only eats n / 2 of them.

---

Alice can eat either minimum of n / 2 or number of different candy types. We
can compute this via converting the given candyType into a set to identify
number of candy types present. This would take O(n) in both time complexity and
space complexity.

---

Python:

```python

class Solution575:

    def distributeCandies(self, candyTypes):

        return min(len(set(candyTypes)), len(candyTypes) / 2)

```
