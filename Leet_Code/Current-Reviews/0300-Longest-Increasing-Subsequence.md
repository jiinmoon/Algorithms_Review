# 300. Longest Increasing Subsequence

Given an integer array nums, return the length of the longest strictly
increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some
or no elements without changing the order of the remaining elements. For
example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

---

#### (1) Brute Force.

One method would be to simply generate all possible subsequences and check for
longest increasing ones. As at each position there are n possibilities, time
complexity would be O(2^n).

#### (2) Maintain longest subsequence with binary search.

Here, we try to build the longest subsequence possible. To do so, we maintain
the longest subsequence that we have seen thus far. For each new value, we
perform binary search for right most value in the resulting array. If the
insertion point has reached out of bound, this marks a new greater element that
can extend our current subsequence. Otherwise, we have to update inner value
where insertion point has been found by minimum of either two. Using this
method, we can update our subsequence in O(log(n)) time. Thus, overall time
complexity would be O(n * log(n)) and space complexity would be O(n).

---

Java: Binary Search Right.

```java

class Solution300 {
    
    List<Integer> result;
    
    public int lengthOfLIS(int[] nums) {

        this.result = new ArrayList<>();
        
        for (int num : nums)
        {
            int ins = binSearchRight(num);
            
            if (ins - 1 == result.size() - 1)
                result.add(num);

            else
                result.set(ins, Math.min(result.get(ins), num));
        }
        
        return this.result.size();
    }
    
    private int binSearchRight(int target)
    {
        int l = 0, r = this.result.size();
        
        while (l < r)
        {
            int m = l + (r - l) / 2;
            
            if (this.result.get(m) >= target)
                r = m;

            else
                l = m + 1;
        }
        
        return r;
    }
}
```
