# 26. Remove Duplicates from Sorted Array

Given a sorted array nums, remove the duplicates in-place such that each
element appears only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying
the input array in-place with O(1) extra memory.

Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means a modification
to the input array will be known to the caller as well.

---

#### (1) Set.

This one also works with non-sorted arrays; bascially, use a set to maintain
a previously seen elements; if we seen current element, we skip over. O(n) in
time complexity and O(n) in space.

#### (2) Two Pointers.

Since the array is already in sorted order, we can use two pointers - one to
denote last insertion point and other to scan across. So long as the new
element encountered is not same as previously inserted value, we insert this
new value to previously inserted index + 1. O(n) in time complxity but O(1) in
space.

---

Java:

```java

class Solution26 {
    
    public int removeDuplicates(int[] nums)
    {
        int i = 0;
        for (int j = 1; j < nums.length; j++)
        {
            if (nums[i] != nums[j])
                nums[++i] = nums[j];
        }
        
        return i+1;
    }
}

```

Java; set.

```java  

class Solution26 {

    public int removeDuplicates(int[] nums) 
    {
        Set<Integer> seen = new HashSet<>();
        
        int ins = 0;
        for (int i = 0; i < nums.length; i++)
        {
            if (!seen.contains(nums[i]))
                nums[ins++] = nums[i];
            seen.add(nums[i]);
        }
        
        return ins;
    }
}

```
