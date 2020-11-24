# Two Sum Unique Pairs

Given an int array nums and an int target, find how many unique pairs in the
array such that their sum is equal to target. Return the number of pairs.

---

One approach would be to first sort the array. Then, we can use two pointers
method starting from beginning and end of the list. If nums[l] + nums[r] is
equal to target, we have found our pair. However, it is entirely possible that
we have a duplicate entries in the array. Hence, we use set data structure to
maintain our unique pairs found thus far. This is O(n * log(n)) in time
complexty and O(n) in space complexity.

Another method is to use two sets. In one of the sets, we maintain a set of
values that we have determined to be a pair thus far. On the other set, we
simply maintain the values that we have seen thus far. Thus, we iterate on
every value to check for the condition where we have seen previously a value of
(target - current value). If the pair sum to target, it should exist in the set
whereas it should not exist in the set of pairs that we have seen thus far.
With this method, the time complexity would reduce to O(n).

---

Java: two sets method.

```java

class Solution {
    
    public int numUniquePairs(int[] nums, int target) {
        HashSet<Integer> result = new HashSet<>();
        HashSet<Integer> prev = new HashSet<>();

        for (int num : nums) {
            if (prev.contains(target - prev) && !result.contains(num)) {
                result.add(target - prev);
                result.add(num);
            }
            prev.add(num);
        }

        return result.size() / 2;
    }
}

```
