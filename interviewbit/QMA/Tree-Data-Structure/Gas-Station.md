# Gas Station

Given two integer arrays A and B of size N.
There are N gas stations along a circular route, where the amount of gas at
station i is A[i].

You have a car with an unlimited gas tank and it costs B[i] of gas to travel
from station i
to its next station (i+1). You begin the journey with an empty tank at one of
the gas stations.

Return the minimum starting gas station’s index if you can travel around the
circuit once, otherwise return -1.

You can only travel in one direction. i to i+1, i+2, … n-1, 0, 1, 2..

Completing the circuit means starting at i and ending up at i again.

---

Iterating through the given arrays, we compute the current amount of fuel left
in the car by moving to i-th station. If the fuel ever goes below 0, we know
that trip is impossible upto this point and we should start over. We can
identify whether we can complete the entire trip by checking to see that
overall amount of gas obtained is greater than amount of costs to travel (net
positive in total).

O(n) in time complexity.

---

Python:

```python

class Solution:

    def canCompleteCircuit(self, A, B):

        start, currFuel, totalFuel = 0, 0, 0

        for i in range(len(A)):
            currFuel += A[i] - B[i]
            totalFuel += A[i] - B[i]

            if currFuel < 0:
                currFuel = 0
                start = i + 1

        return start if totalFuel >= 0 else -1

```


