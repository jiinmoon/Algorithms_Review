# 128. Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest
consecutive elements sequence.

Follow up: Could you implement the O(n) solution? 

---

Create a set of integers so that we can look up its membership in O(1). For
each number we examine, we iterate as far out as possible while incrementing
current number and record its length to find the maximum amongst them.

Time and space complexity would be O(n).

---

Java:

```java

class Solution128 {

    public int longestConsecutive(int[] nums)
    {
        Set<Integer> numSet = new HashSet<>();
        for (int num : nums)
            numSet.add(num);

        int currLen = 0, maxLen = 0;

        for (int num : numSet)
        {
            // already processed previously
            if (numSet.contains(num - 1))
                continue;

            currLen = 0;
            while (numSet.contains(num++))
                currLen++;
            maxLen = max(maxLen, currLen);
        }
        return maxLen;
    }
}

```
