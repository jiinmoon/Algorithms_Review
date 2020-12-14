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


Let's try an example:

```
(1) arr = [1, 2, 1, 5]

    Step:1      
        
        Current element is 1 and our result is empty; add.

                curr    =   1
                result  =   [1]
    
    Step:2

        Current element is 2 and it can extend; add.

                curr    = 2
                result  = [1, 2]

    Step:3

        Current element is 1 and it is smaller; looking back, 1 replaces 1.

                curr    = 1
                result  = [1, 2]

    Step:4

        Current element is 5 and it can extend; add.

                curr    = 5
                result  = [1, 2, 5]

---

(2) arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

    Step:1
        
                curr    = 0
                    -> binSearch(0) = 0
                result  = [0]

    Step:2

                curr    = 8
                    -> binSearch(8) = 1
                result  = [0, 8]

    Step:3
                
                curr    = 4
                result  = [0, 4]

    Step:4
                
                curr    = 12
                result  = [0, 4, 12]

    Step:5
                
                curr    = 2
                    -> binSearch(2) = 1
                result  = [0, 2, 12]

    Step:6

                curr    = 10
                result  = [0, 2, 10]

    Step:7

                curr    = 6
                result  = [0, 2, 6]

    ...
```

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
