# 238. Product of Array Except Self

Given an array nums of n integers where n > 1,  return an array output such
that output[i] is equal to the product of all the elements of nums except
nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or
suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not
count as extra space for the purpose of space complexity analysis.)

---

The problem is much easier to visualize as follows: suppose that we are given
a list of [a, b, c, d]. Then, we know that end result must of [bcd, acd, abd,
abc].

To generate the end result, we first iterate the create a product from left to
right as follows:

[a, b, c, d]
[1, a, ab, abc]

Then, upon this result list, we iterate from right to left, multiplying from
original list again.

[1, a, ab, abc]
[bcd, acd, abd, abc]

---

Java:

```java

class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] result = new int[nums.length];
        result[0] = 1;
        for (int i = 0; i < nums.length - 1; i++)
            result[i+1] = result[i] * nums[i];

        int temp = 1;
        for (int i = nums.length - 1; i >= 0; i--) {
            result[i] *= temp;
            temp *= nums[i];
        }
        return result;
    }
}
```

Python:

```python

class Solution:
    def productExceptSelf(self, nums):
        result = [1]
        for num in nums[1:]:
            result.append(result[-1] * num)

        product = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= product
            product *= nums[i]
        return reuslt
```
