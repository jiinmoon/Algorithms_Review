# 134. Gas Station

There are N gas stations along a circular route, where the amount of gas at
station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel
from station i to its next station (i+1). You begin the journey with an empty
tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit
once in the clockwise direction, otherwise return -1.

Note:

If there exists a solution, it is guaranteed to be unique.
Both input arrays are non-empty and have the same length.
Each element in the input arrays is a non-negative integer.

---

From each of the station (index), we try to traverse. We may only complete the
route only when sum(gas) is greater than or equal to the sum(cost).

While maintaing our current amount of fuel, we traverse. At each station, we
check the net gain of gas to cost. After updating this net gain to our fuel, if
it goes negative, we know that this station cannot be starting point. Thus, we
reset and repeat the process.

Time complexity should be O(n) and space complexity is O(1).

---

Java:

```java

class Solution {
        
    public boolean canCompleteCircuit(int[] gas, int[] cost) {
        int startStation, currFuel, totalBalance;
        startStation = currFuel = totalBalance = 0;

        for (int i = 0; i < gas.length(); i++) {
            int netGain = gas[i] - cost[i];
            currFuel += netGain;
            totalBalance += netGain;
            if (currFuel < 0) {
                startStation = i + 1;
                currFuel = 0;
            }
        }

        // can only complete when total balance of fuel after traversing is positive
        return (totalBalance > 0) ? startStation : -1;
    }
}
