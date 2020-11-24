# 167. Two Sum II

Given an array of integers that is already sorted in ascending order, find two
numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add
up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not
use the same element twice.

---

Since the elements are sorted, we can use two pointers method to find the pair
that add up to target number in a single interation. Have a pointer at start
and end. If their sum equals to target, (start+1, end+1) is our result.
Otherwise, we check that current sum is less than or greater than target; if it
is less than, than we need to increment start as we want to consider larger
value for our next candidate and vice versa.

---

Java:

```java

class Solution {
    
    public int[] twoSum(int[] nums, int target) {

        int l = 0, r = nums.length - 1;

        while (l < r) {
            int currSum = nums[l] + nums[r];
            if (currSum == target) {
                return new int[] { l+1, r+1 };
            } else if (currSum < target) {
                l++;
            } else {
                r--;
            }
        }

        return new int[] {};
    }
}

```
