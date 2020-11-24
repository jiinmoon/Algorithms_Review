# 169. Majority Element

Given an array of size n, find the majority element. The majority element is
the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always
exist in the array.

---

Naive approach to this problem would be to count each occurrence of the
elements and return the element that appears more than floor(n/2) times. This
would require additional O(n) space and can complete in O(n) time complexity.

To improve upon this, we use majority voting algorithm. Here, we maintain
a candidate and current candidate count. As we exaimne each index and its
candidate, we check that previously selected candidate was repeated again. In
this case, we increase our count. Otherwise, different candidate has been voted
so we decrease the count. When the count reaches 0, we switch to the current
candidate that has been voted. This does not require additional space but can
complete in O(n) time complexity.

---

Java:

```java

class Solution {

    public int majorityElement(int[] nums) {
        int curr = Integer.MAX_VALUE;
        int votes = 0;

        for (int num : nums) {
            if (votes == 0)
                curr = num;

            if (curr == num)
                count++;
            else
                count--;
        }

        return curr;    // majority element is gurantee'd; otherwise check MAX_VALUE;
    }
}

```
