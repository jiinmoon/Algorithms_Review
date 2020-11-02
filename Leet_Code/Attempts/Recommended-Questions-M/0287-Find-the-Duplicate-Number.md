# 287. Find the Duplicate Number

Given an array of integers nums containing n + 1 integers where each integer is
in the range [1, n] inclusive.

There is only one duplicate number in nums, return this duplicate number.

Follow-ups:

How can we prove that at least one duplicate number must exist in nums? 
Can you solve the problem without modifying the array nums?
Can you solve the problem using only constant, O(1) extra space?
Can you solve the problem with runtime complexity less than O(n2)?

---

The simplest solution would be to use the extra space where we can record the
previously encountered values. Once we encounter the duplicate by checking
against the record, we can return the duplciate value. Using hashmap, lookup
should be O(1), thus the algorithm can complete in O(n). However, this approach
requires additional space in which is suboptimal.

Another apporach is utilize the particular nature of the given array such that
where each of the integers appearing is bounded to the length of the array.
Hence, we can use the array and the index as the marker to find the duplicate
element. However, while this will not require additional space, it does
indicate the modification of the given array inplace.

Upon further examination, we can further improve the algorithm once we realize
that for each integer, its nums[index] should also be present. Thus, this
problem becomes a cycle detection problem where we try to move the index
forward until we come at the same place. Once cycle is found, we find the
starting position of where the cycle occurs by searching from start again. In
this approach, we can find the duplicate in O(n) without additional space and
without modifying the given array.

---

Python:

```python

class Solution:
    def findDuplicate(self, nums):
        # set up runners
        slow = nums[0]
        fast = nums[slow]
        
        # fast moves twice as faster than slow
        # guranteed to terminate
        while fast != slow:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        curr = 0
        while curr != slow:
            curr = nums[curr]
            slow = nums[slow]

        return curr
```
