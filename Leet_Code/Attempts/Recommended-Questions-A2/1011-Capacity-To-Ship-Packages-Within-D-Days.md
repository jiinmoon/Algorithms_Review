# 1011. Capacity To Ship Packages Within D Days

A conveyor belt has packages that must be shipped from one port to another
within D days.

The i-th package on the conveyor belt has a weight of weights[i].  Each day, we
load the ship with packages on the conveyor belt (in the order given by
weights). We may not load more weight than the maximum weight capacity of the
ship.

Return the least weight capacity of the ship that will result in all the
packages on the conveyor belt being shipped within D days.

---

We can think of this problem as a binary search problem where we are trying to
find the right capacity to ship the packages within the allowed days. The
minimum capacity of the ship required would be the maximum of the weights. The
maximum would be total sum of all weights. Then, perform binary search for
middle ground and check that whether it is indeed shipable within D days.

Time complexity would be O(n * log(n)). For each mid found, we have to process
all weights to check to see whether it is shipable.

---

Java:

```java

class Solution1011 {

    private int[] weights;
    private int D;

    public int shipWithinDays(int[] weights, int D)
    {
        this.weights = weights;
        this.D = D;

        int min_cap = 0, max_cap = 0;

        for (int weight : weights)
        {
            min_cap = Math.max(min_cap, weight);
            max_cap += weight;
        }
        
        // bin search as far left as possible
        while (min_cap < max_cap)
        {
            int mid_cap = min_cap + (max_cap - min_cap) / 2;

            if (isShipable(mid_cap))
                max_cap = mid_cap;
            else
                min_cap = mid_cap + 1;
        }

        return min_cap;
    }

    private boolean isShipable(int cap)
    {
        int days = this.D, currLoad = 0;

        for (int weight : this.weights)
        {
            // if ship load exceeds by loading current weight
            // another shipment is required
            if (currLoad + weight > cap) {
                currLoad = 0;
                days--;
            }
            // more weights to process but ran out of days
            if (days == 0)
                return false;
        }

        return true;
    }
}

```
