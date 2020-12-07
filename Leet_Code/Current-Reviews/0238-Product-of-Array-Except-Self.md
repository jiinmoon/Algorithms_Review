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

---

Let us visualize this with an example:

    Suppose we have a given array [ A, B, C, D ].

    Then, we can first prepare our result array by cumulative product to its
    right first.

        [ 1, A, AB, ABC ]

    Then, we perform the same operations but in opposite directions.

        [ BCD, ACD, ABD, ABC ]

Time complexity would be O(n) and space would be O(n) to create a resulting
list.

---

Java:

```java

class Solution238 {

    public int[] productExceptSelf(int[] nums)
    {
        int[] result = new int[nums.length];
        result[0] = 1;

        // cumulative product to right
        for (int i = 0; i < nums.length-1; i++)
            result[i+1] = result[i] * nums[i];

        // opposite direction
        int temp  = 1;
        for (int i = nums.length - 1; i >= 0; i--)
        {
            result[i] *= temp;
            temp *= nums[i];
        }

        return result;
    }
}

```
