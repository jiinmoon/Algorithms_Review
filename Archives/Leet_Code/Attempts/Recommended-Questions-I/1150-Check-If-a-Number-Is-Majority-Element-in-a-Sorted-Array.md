# 1150. Check If a Number Is Majority Element in a Sorted Array

Given an array nums sorted in non-decreasing order, and a number target, return
True if and only if target is a majority element.

A majority element is an element that appears more than N/2 times in an array
of length N.

---

Naive approach would be to iterate to count the number of times that target
appears; once the count reaches above N/2 times, we can return true. This would
be O(n) in time complexity.

We can improve it further by using binary search algorithm. We can search for
leftmost and rightmost index of where the target element would be, then check
whether this window size exceeds the size of N/2. This is O(log(n)) in time
complexity.

---

Java: binary search approach.

```java

class Solution {
    
    public boolean majorityElement(int[] nums, int target) {
        int left = binSearchLeft(nums, target, 0, nums.length);
        int right = binSearchRight(nums, target, 0, nums.length);
        return (right - left) > nums.length / 2;
    }

    private int binSearchLeft(int[] nums, int target, int l, int r) {
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] < target)     l = mid + 1;
            else                        r = mid;
        }
        return l;
    }

    private int binSearchRight(int[] nums, int target, int l, int r) {
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] > target)     r = mid;
            else                        l = mid + 1;
        }
        return r;
    }
}

```

Java: naive counting approach.

```java

class Solution {
    
    public boolean majorityElement(int[] nums, int target) {
        int count = 0;
        for (int num : nums) {
            if (num == target) count++;
            if (count > nums.length) return true;
        }
        return false;
    }
}

```
