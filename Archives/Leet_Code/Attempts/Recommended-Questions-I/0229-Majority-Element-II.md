# 229. Majority Element II

Given an integer array of size n, find all elements that appear more than ⌊ n/3
⌋ times.

Follow-up: Could you solve the problem in linear time and in O(1) space?

---

Naive solution involves an additional O(n) space to count occurrences of each
elements, and collect those which appear more than floor(n/3) times. This is
O(n) in time complexity.

Another method is using the majority voting algorithm. Here, we note that there
may only be two viable candidates for elements appear more than floor(n/3)
times. Hence, we modify our voting algorithm to find the two candidates
instead. This does not require additional space but completes in O(n) time
complexity.

---

Java:

```java

class Solution {

    public List<Integer> majorityElement(int[] nums) {
        int candidate1 = Integer.MAX_VALUE;
        int votes1 = 0;
        int candidate2 = Integer.MAX_VALUE;
        int votes2 = 0;

        for (int num : nums) {
            if (candidate1 == num)          votes1++;
            else if (candidate2 == num)     votes2++;
            else if (count1 == 0) {
                candidate1 = num;
                votes1 = 1;
            } else if (count2 == 0) {
                candidate2 = num;
                votes1 = 1;
            } else {
                votes1--;
                votes2--;
            }
        }

        // there is no gurantee that candidates are indeed majority
        // confirm by counting each candidates
        votes1 = votes2 = 0;
        List<Integer> result = new LinkedList<>();
        for (int num : nums) {
            if (candidate1 == num) votes1++;
            if (candidate2 == num) votes2++; }

        if (votes1 > nums.length / 3) result.add(candidate1);
        if (votes2 > nums.length / 3) result.add(candidate2);
        
        return result;
    }
}

```
