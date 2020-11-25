# 53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least
one number) which has the largest sum and return its sum.

Follow up: If you have figured out the O(n) solution, try coding another
solution using the divide and conquer approach, which is more subtle.

---

We iterate forward to build our contiguous subarray. For every value that we
consider, we try to add to our current contiguous subarray. If the sum becomes
smaller, then adding new value breaks our contiguous subarray. Amongst all
subarray considered, we choose the maximum.

Time complexity would be O(n) and space complexity would be O(1).

---

Java:

```java

class Solution {

    public int maximumSubarray(int[] nums)
    {
        if (nums.length == 0)
            return 0;

        int currSum = 0, maxSum = Integer.MIN_VALUE;

        for (int num : nums)
        {
            currSum = Math.max(currSum + num, num);
            maxSum = Math.max(currSum, maxSum);
        }

        return maxSum;
    }
}

```
