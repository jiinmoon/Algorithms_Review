# 1396. Design Underground System

Implement the class UndergroundSystem that supports three methods:

1. checkIn(int id, string stationName, int t)

A customer with id card equal to id, gets in the station stationName at time t.
A customer can only be checked into one place at a time.

2. checkOut(int id, string stationName, int t)

A customer with id card equal to id, gets out from the station stationName at
time t.

3. getAverageTime(string startStation, string endStation) 

Returns the average time to travel between the startStation and the endStation.
The average time is computed from all the previous traveling from startStation
to endStation that happened directly.

Call to getAverageTime is always valid.

You can assume all calls to checkIn and checkOut methods are consistent. That
is, if a customer gets in at time t1 at some station, then it gets out at time
t2 with t2 > t1. All events happen in chronological order.

---

We design this system as using hashmaps to store information about pair of
startStation and endStation and their total times traveled and number of times
that trip has been made. By doing so, we can achieve O(1) in time complexity
for all methods and O(n^2) for space complexity as we are storing every station
pairs.

---

Python:

```python

class Solution1396:

    def __init__(self):
        self.checkIns = dict()
        self.stationTimeCounter = dict()

    def checkIn(self, id, startStation, startTime):
        self.checkIns[id] = (startStation, startTime)

    def checkOut(self, id, endStation, endTime):
        startStation, startTime = self.checkIns.pop(id)

        currStation = (startStation, endStation)
        currTime = endTime - startTime

        self.d.setdefault(currStation, [0, 0])
        self.d[currStation][0] += currTime
        self.d[currStation][1] += 1

    def getAverageTime(self, startStation, endStation):
        currStation = (startStation, endStation)

        if currStation in self.d:
            travelTime, totalCount = self.d[currStation]
            return travelTime / totalCount
```
