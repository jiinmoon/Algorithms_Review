# 189. Rotate Array

Given an array, rotate the array to the right by k steps, where k is
non-negative.

Follow up:

Try to come up as many solutions as you can, there are at least 3 different
ways to solve this problem.
Could you do it in-place with O(1) extra space?

---

Naive approach would be to prepare a new array to add the elements at its
correct indicies as determined by (i + k) % len(array). Then, move over from
temp array to new array. This requires additional O(n) space. But completes in
O(n) time complexity.

Another approach would be to perform shift as many times as needed for k times.
This can be done in-place but would be O(k * n) time complexity.

If the elements were gurantee'd to be positive, we can swap the insertion point
of each element to its correct place and mark it as finished by negating it.
This can be done in O(n) without additional space, but does not work with
negative numbers.

Another approach would be reversing the elements - first reverse the entire
array, then reverse on lower half upto k and reverse again on uppoer half. This
would be O(n) without additional space.

---

Java : reversing approach.

```java

class Solution {
    public void rotate(int[] nums, int k) {
        k = k % nums.length;
        reverse(nums, 0, nums.length-1);
        reverse(nums, 0, k-1);
        reverse(nums, k, nums.length-1);
    }
    
    public void reverse(int[] nums, int start, int end) {
        while (start < end) {
            int temp = nums[start];
            nums[start++] = nums[end];
            nums[end--] = temp;
        }
    }
}

```
