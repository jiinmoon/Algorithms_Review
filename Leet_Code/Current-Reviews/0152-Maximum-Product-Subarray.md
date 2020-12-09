# 152. Maximum Product Subarray

Given an integer array nums, find the contiguous subarray within an array
(containing at least one number) which has the largest product.

---

The problem here is the negative number which can result in greater product
when it is multiplied by another negative number. If this is the case, then we
maintain both the maximum positive and the minimum negative contiguous subarray
product as we iterate. For each element encountered, either element itself will
be most positive or negative (which breaks the array); or it can product
further greater positive or negative product subarray. 

Time complexity would be O(n) and space is O(1).

---

Java:

```java

class Solution152 {

    public int maxProduct(int[] nums) {
        
        int maxPos = 1, minNeg = 1, result = Integer.MIN_VALUE;
        
        for (int num : nums)
        {
            int tempMaxPos = maxPos;
            maxPos = Math.max(num, Math.max(tempMaxPos * num, minNeg * num));
            minNeg = Math.min(num, Math.min(tempMaxPos * num, minNeg * num));
            
            result = Math.max(result, maxPos);
        }
        
        return result;
    }
}

```
