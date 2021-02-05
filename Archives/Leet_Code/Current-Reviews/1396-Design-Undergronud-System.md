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

Use two hashmap; one to track the check-in/check-out by the id; and other to
track the (start, end) stations total time traveled and counts.

O(1) in time complexity for all methods.

---

Python:

```python

class Solution1396:

    def __init__(self):

        self.check_ins = dict()
        self.station_times = dict()


    def checkIn(self, id, startStation, startTime):
        
        self.check_ins[id] = (startStation, startTime)

    
    def checkOut(self, id, endStation, endTime):

        startStation, startTime = self.check_ins[id]
        station = (startStation, endStation)
        
        self.station_times.setdefault(station, (0, 0))

        self.station_times[station][0] += endTIme - startTime
        self.station_times[station][1] += 1


    def getAverageTime(self, startStation, endStation):
        
        station = (startStaion, endStation)

        if station in self.station_times:
            totalTime, count = self.station_times[station]
            return totalTime / count

```


